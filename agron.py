from  .extension import create_app

from .home import main
from .service.farmer import farmer
from .invest import invest
from .shop import shop
from .auth import auth
from .models import user

app = create_app()

app.register_blueprint(main)
app.register_blueprint(farmer)
app.register_blueprint(invest)
app.register_blueprint(shop)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)