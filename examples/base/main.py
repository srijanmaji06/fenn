from fenn import FENN
from fenn.notification.services import Discord, Telegram

app = FENN()
app.register_notification_services([Discord, Telegram])

@app.entrypoint
def main(args):

    # 'args' contains your fenn.yaml configurations
    message = f"Training with learning rate: {args['training']['lr']}"

    app.notify(message)
    print(message)

    # Your logic here...

if __name__ == "__main__":
    app.run()