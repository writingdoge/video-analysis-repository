from flask import Flask, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session

from exts import db
import settings
import apps.models


# 配置和创建 Flask 应用实例
# Flask 应用创建与配置：

# app = Flask(__name__, template_folder='../templates', static_folder='../static')：创建 Flask 应用实例，并指定模板和静态文件的目录。
# app.config.from_object(settings.DevelopmentConfig)：从 settings.DevelopmentConfig 加载应用配置。
# 其他配置项如 SQLALCHEMY_TRACK_MODIFICATIONS、SESSION_TYPE 和 SESSION_PERMANENT 等也在此处设置。
# 会话管理：

# Session(app)：使用 flask_session 来管理会话数据，支持将会话数据存储在文件系统中，路径为 ./flask_session/。
# 数据库管理：

# db.init_app(app)：初始化 SQLAlchemy 数据库绑定，允许 Flask 应用与数据库进行交互。
# migrate = Migrate(app, db)：集成 Flask-Migrate，支持数据库迁移管理。
# 跨域资源共享（CORS）：

# CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)：启用 CORS，允许来自任何源的请求访问 /api/* 路径下的资源，并支持携带凭据。


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = './flask_session/'  # 保存session的文件夹路径
    app.config['SESSION_PERMANENT'] = False  # 确保会话不过期
    Session(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    return app
