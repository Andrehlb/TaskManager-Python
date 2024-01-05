from flask import Flask, render_template, request, redirect, url_for, flash
from models import Task
from database import db_session

app = Flask(__name__)
app.secret_key = 'sua_chave secreta_aqui'

@app.route('/create-task', methods=['GET', 'POST'])
def create_task():
    if request.method =='POST':
        # aqui está a lógica para processar os dados do formulário.
        task_description = request.form.get('description')
        task_due_date = request.form.get('due_date')
        task_priority = request.form.get('priority')

        # Aqui fazer a validade dos dados
        if not task_description:
            flash('É obrigatório fazer a  descrição!', 'error')
            return redirect(url_for('create_task'))
        
        # Criação e inserção no banco de dados usando SQLAlchemy
        new_task = Task(description=task_description, due_date=task_due_date, task_priority=task_priority)
        db_session.add(new_task)
        db_session.commit()

        flash('Tarefa criada com sucesso! ', 'success')
        return redirect(url_for('create_task')) # Ou redirecionar para a página, conforme necessário.
    
    return render_template('create_task.html    ')

if __name__ == '__main__':
    app.run(debug=True)from flask import Flask, render_template, request, redirect, url_for, flash
from models import Task
from database import db_session

app = Flask(__name__)
app.secret_key = 'sua_chave secreta_aqui'

@app.route('/create-task', methods=['GET', 'POST'])
def create_task():
    if request.method =='POST':
        # aqui está a lógica para processar os dados do formulário.
        task_description = request.form.get('description')
        task_due_date = request.form.get('due_date')
        task_priority = request.form.get('priority')

        # Aqui fazer a validade dos dados
        if not task_description:
            flash('É obrigatório fazer a  descrição!', 'error')
            return redirect(url_for('create_task'))
        
        # Criação e inserção no banco de dados usando SQLAlchemy
        new_task = Task(description=task_description, due_date=task_due_date, task_priority=task_priority)
        db_session.add(new_task)
        db_session.commit()

        flash('Tarefa criada com sucesso! ', 'success')
        return redirect(url_for('create_task')) # Ou redirecionar para a página, conforme necessário.
    
    return render_template('create_task.html    ')

@app.route('/tasks')
def list_tasks():
    tasks = db_session.query(Task).all()
    return render_template('list_tasks.html', tasks=tasks)

@app.route('/update-task/<int:task_id>', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)