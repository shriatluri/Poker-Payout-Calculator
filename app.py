from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import pandas as pd
import io
import flask

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

players = []
default_buy_in = 50  # Default buy-in amount

@app.route('/')
def index():
    return render_template('index.html', players=players, default_buy_in=default_buy_in)

@app.route('/add_player', methods=['POST'])
def add_player():
    name = request.form['name']
    buy_in = float(request.form['buy_in'])
    players.append({'name': name, 'buy_in': buy_in, 'end_amount': 0})
    return redirect(url_for('index'))

@app.route('/add_default_buy_in/<player_name>', methods=['POST'])
def add_default_buy_in(player_name):
    for player in players:
        if player['name'] == player_name:
            player['buy_in'] += default_buy_in
    return redirect(url_for('index'))

@app.route('/remove_default_buy_in/<player_name>', methods=['POST'])
def remove_default_buy_in(player_name):
    for player in players:
        if player['name'] == player_name:
            player['buy_in'] -= default_buy_in
            if player['buy_in'] < 0:
                player['buy_in'] = 0
    return redirect(url_for('index'))

@app.route('/edit_buy_in/<player_name>', methods=['POST'])
def edit_buy_in(player_name):
    new_buy_in = float(request.form['new_buy_in'])
    for player in players:
        if player['name'] == player_name:
            player['buy_in'] = new_buy_in
            flash(f'Updated {player_name}\'s buy-in amount to ${new_buy_in:.2f}', 'success')
    return redirect(url_for('index'))

@app.route('/set_default_buy_in', methods=['POST'])
def set_default_buy_in():
    global default_buy_in
    default_buy_in = float(request.form['default_buy_in'])
    return redirect(url_for('index'))

@app.route('/finalize', methods=['POST'])
def finalize():
    total_buy_in = sum(player['buy_in'] for player in players)
    total_end_amount = sum(float(request.form[f'end_amount_{player["name"]}']) for player in players)
    
    if total_buy_in != total_end_amount:
        flash(f'Total end amount (${total_end_amount:.2f}) does not match total buy-in (${total_buy_in:.2f}). Please check your inputs.', 'error')
        return redirect(url_for('index'))
    
    for player in players:
        player['end_amount'] = float(request.form[f'end_amount_{player["name"]}'])
    return redirect(url_for('results'))

@app.route('/results')
def results():
    payouts = calculate_payouts(players)
    return render_template('results.html', payouts=payouts)

@app.route('/edit')
def edit():
    return redirect(url_for('index'))

@app.route('/download')
def download():
    output = io.BytesIO()
    df = pd.DataFrame(players)
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Players')
    output.seek(0)
    
    if flask.__version__ >= "2.0.0":
        return send_file(output, download_name="players.xlsx", as_attachment=True)
    else:
        return send_file(output, attachment_filename="players.xlsx", as_attachment=True)

def calculate_payouts(players):
    balances = {player['name']: player['end_amount'] - player['buy_in'] for player in players}
    creditors = sorted((name for name, balance in balances.items() if balance > 0), key=lambda x: -balances[x])
    debtors = sorted((name for name, balance in balances.items() if balance < 0), key=lambda x: balances[x])

    payouts = []
    while creditors and debtors:
        creditor = creditors[0]
        debtor = debtors[0]
        credit_amount = balances[creditor]
        debt_amount = -balances[debtor]

        amount = min(credit_amount, debt_amount)
        payouts.append(f'{debtor} owes {creditor} ${amount:.2f}')

        balances[creditor] -= amount
        balances[debtor] += amount

        if balances[creditor] == 0:
            creditors.pop(0)
        if balances[debtor] == 0:
            debtors.pop(0)

    return payouts

if __name__ == '__main__':
    app.run(debug=True)
