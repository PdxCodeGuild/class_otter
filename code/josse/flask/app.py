from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "How to survive PDX Coding Bootcamp",
        'author': "josse perez",
        'date': "February 7, 2022",
        'body': "Artisan Mini-Mart Kale baby flannel more rain animal welfare charcuterie chicken coop game nights patchouli handcrafted Hood to Coast freegans small plates Silicon Forest Hawthorne. Por Que No? Alberta Arts unicycling with bagpipes and Darth Vader mask The Bins Last Thursday punk rock Vera Katz dog parks Grimm <br> soy ink tattoos rain West End evergreens it's raining again IPA no, you go. Pickled Mt. St. Helens blackberries Tasty & Sons Pine Street Market vegan meatball sub brunch lines Forest Park breweries Harvey Milk Street dreadlocks gluten free moustache Salt and Straw. yupster nanobrewery late-night happy hours UGB Mount Tabor vegan DIY tall bikes muesli Doug Fir vintage snowpacolypse new urbanist Impossible Burger patio."
    },

    {
        'title': "Cheesy smells blog",
        'author': "liz",
        'date': "February 8, 2022",
        'body': "Tote bag tousled banh mi everyday carry. Live-edge cronut austin, tumblr pop-up salvia ennui tacos thundercats. Intelligentsia hella scenester mixtape, jean shorts <br> iceland authentic. Semiotics disrupt food truck pabst ugh meggings leggings."

    },

    {'title': "Crazy cat blog",
        'author': "merritt",
        'date': "February 8, 2022",
        'body': "I'm baby selvage kickstarter ramps, pitchfork neutra blog leggings readymade quinoa. Vegan polaroid bespoke you probably haven't heard of them drinking vinegar. Selfies ethical venmo heirloom, brooklyn kogi you probably haven't heard of them four loko. Ramps swag tousled squid pop-up mixtape, cray tattooed truffaut twee.<br> Ethical tousled coloring book wayfarers farm-to-table. Selvage fixie chillwave chambray scenester succulents. Echo park raw denim keffiyeh skateboard cliche tilde."

     },

    {'title': "Python for everyone",
        'author': "Author",
        'date': "February 8, 2022",
        'body': "I'm baby selvage kickstarter ramps, pitchfork neutra blog leggings readymade quinoa. Vegan polaroid bespoke you probably haven't heard of them drinking vinegar. Selfies ethical venmo heirloom, brooklyn kogi you probably haven't heard of them four loko. Ramps swag tousled squid pop-up mixtape, cray tattooed truffaut twee. <br>Ethical tousled coloring book wayfarers farm-to-table. Selvage fixie chillwave chambray scenester succulents. Echo park raw denim keffiyeh skateboard cliche tilde."


     }
]


@app.route('/')
def index():
    return render_template("index.html", posts=posts)


app.run(debug=True)
