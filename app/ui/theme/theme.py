from nicegui import ui


def theme():

    # Follow system light/dark preference
    ui.dark_mode().auto()


    ui.add_head_html(
        """
        <style>

        body {
            font-family:
            Inter,
            system-ui,
            sans-serif;
        }


        .dashboard-card {

            border-radius: 20px;

            padding: 20px;

            transition:
            transform .2s ease,
            box-shadow .2s ease;

        }


        .dashboard-card:hover {

            transform:
            translateY(-4px);

            box-shadow:
            0 10px 30px
            rgba(0,0,0,.15);

        }


        </style>
        """
    )