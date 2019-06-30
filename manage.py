from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Category, Pitch, Comment, Role


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db,
                User=User, Category=Category, Pitch=Pitch, Comment=Comment, Role=Role)


if __name__ == '__main__':
    manager.run()
