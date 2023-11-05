from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/create-task', methods=['GET', 'POST'])
def creart_task():
    if request.method =='POST':
        # aqui está a lógica para processar os dados do formulário.
        pass
    return render_template('create_task.html    ')

if __name__ == '__main__:
app.run(debug=True)