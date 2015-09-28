<!DOCTYPE html>
<html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link type="text/css" rel="stylesheet" href="/assets/bootstrap.min.css" />

        <style type="text/css">
            #video {
                width: 100%;
                margin: 0 0 10px 0;
            }

            form {
                margin: 0 0 10px 0;
            }

            .display {

            }
            .display .row {
                height: 25px;
            }
            .display .row .cell {
                width: 6.25%;
                height: 25px;
                float: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Message List</h1>

            <ul class="list-group">
                %for message in messages:
                <li class="list-group-item">{{message.message}} <span class="badge">{{message.name}}</span></li>
                %end
            </ul>
        </div>
    </body>
</html>
