from FlaskApp.FlaskApp import FlaskApp

# Utworzenie instancji aplikacji Flask jako Singleton
app_instance: FlaskApp = FlaskApp()

if __name__ == "__main__":
    app_instance.run()