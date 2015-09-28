<!DOCTYPE html>
<html>
    <head>
        <title>Message Form</title>

        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="/assets/bootstrap.min.css" />

        <script type="text/javascript">

            function postForm(form) {
                var url = '/db/messages';

                var xhr = new XMLHttpRequest();
                xhr.open('POST', url, true);
                xhr.send(JSON.stringify(form));

                alert('Your message has been received, thank you');
            }

            window.addEventListener('load', function() {
                var submitButton = document.querySelector('#submitButton');
                var name = document.querySelector('#name');
                var message = document.querySelector('#message');

                submitButton.addEventListener('click', function() {
                    postForm({ name: name.value, message: message.value });

                    name.value = '';
                    message.value  = '';
                });
            });

        </script>
    </head>
    <body>
        <div class="container-fluid">
            <div class="col-md-12">
                <div>
                    <h1>The Helpful Radio Drone</h1>

                    Send messages to our amazing drone
                </div>

                <br />

                <form method="post">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" class="form-control" id="name" placeholder="Name">
                    </div>
                    
                    <div class="form-group">
                        <label for="msg">Message</label>
                        <textarea class="form-control" rows="3" name="msg" id="message" placeholder="Enter your message here..."></textarea>
                    </div>

                    <div class="checkbox">
                        <label>
                            <input type="checkbox" name="public"> Public
                        </label>
                    </div>

                    <button type="button" class="btn btn-primary btn-lg" id="submitButton">Send</button>
                </form>
            </div>
        </div>
    </body>
</html>
