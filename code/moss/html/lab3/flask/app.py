from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    
    posts = [
    
    {"title": "Austin Unicorn",
    "author":"Johnny Appleseed",
    "date": "11/12/21", 
    "body": "Dolore umami reprehenderit, heirloom in messenger bag succulents flannel marfa disrupt next level organic sartorial knausgaard live-edge. You probably haven't heard of them chartreuse fashion axe esse ex subway tile. Iceland squid whatever kitsch hot chicken vegan. Austin unicorn XOXO VHS kogi seitan vape kitsch. Organic unicorn shoreditch, proident affogato flexitarian dreamcatcher locavore blue bottle sed. Pork belly williamsburg chia, in locavore quinoa direct trade. Vape gochujang pitchfork tote bag etsy.Narwhal keytar cupidatat, vegan tumblr cold-pressed shabby chic tbh artisan. Health goth viral taxidermy fugiat cupidatat kickstarter echo park glossier irure cliche fanny pack before they sold out ethical ut. 3 wolf moon pug dolore prism, et polaroid echo park chartreuse iPhone keytar williamsburg non. Master cleanse kickstarter mixtape qui aliqua migas." }, 
    
    {"title":"Etsy XOXO", 
    "author":"12/22/21",
     "body":"Activated charcoal listicle artisan in, plaid palo santo la croix waistcoat kinfolk semiotics tofu pinterest labore aliquip. Anim aute everyday carry hot chicken tbh typewriter. Four dollar toast locavore laborum, cornhole cold-pressed sint health goth man braid. Woke eiusmod cillum officia sriracha iPhone. Blog kickstarter messenger bag, beard meh subway tile four dollar toast cillum tousled squid. Id veniam labore tattooed cold-pressed, lyft DIY typewriter chia echo park reprehenderit venmo wolf marfa cupidatat. Ad actually wayfarers migas nisi meditation excepteur irure skateboard asymmetrical next level cloud bread incididunt kickstarter tbh. Etsy XOXO fashion axe photo booth hella cornhole. Enamel pin yr organic hexagon 8-bit. Put a bird on it fingerstache organic small batch, hella normcore velit mustache forage twee coloring book qui plaid eiusmod. Pug ethical kitsch air plant, exercitation kombucha green juice mollit crucifix yr." },
    
    {"title": "Chia Biodiesel",
    "author":"Roka Garvy",
    "date":"1/26/22",
    "body":"Minim pickled slow-carb authentic leggings retro vinyl, esse est godard ullamco pork belly cillum keffiyeh bushwick. Sriracha freegan retro, pork belly labore cronut locavore put a bird on it aute keytar whatever nisi copper mug enim. In ut hashtag, tilde sed dolore street art single-origin coffee shaman enamel pin flannel umami pinterest retro. Vinyl everyday carry put a bird on it keffiyeh master cleanse you probably haven't heard of them, art party photo booth consectetur aesthetic et +1 ut chicharrones disrupt.Hell of heirloom yuccie fam chartreuse sartorial kickstarter ullamco magna. Lomo slow-carb semiotics viral lorem marfa. Meh PBR&B et, wayfarers migas austin tumeric occupy health goth helvetica coloring book tumblr. Before they sold out consectetur whatever literally cray echo park post-ironic." },
    
    {"title": "Magna Dreamcatcher",
    "author":"Warby Parker",
     "date":"2/1/22", 
     "body":"Ennui anim banh mi eiusmod, meditation keytar humblebrag narwhal. In chia biodiesel sed, gentrify excepteur af food truck art party aesthetic keytar wolf craft beer fashion axe. Farm-to-table subway tile freegan tumblr normcore, meggings franzen pop-up narwhal duis man braid esse banh mi typewriter commodo. Next level ex gastropub, literally green juice swag disrupt 3 wolf moon.Tousled mlkshk gochujang subway tile butcher venmo sartorial typewriter pop-up cronut. Taiyaki minim in kombucha fixie. Godard kogi voluptate, tilde roof party poke vape health goth humblebrag keffiyeh +1 venmo pinterest. Tote bag semiotics non, tumeric literally gochujang reprehenderit freegan subway tile dolore photo booth hella ramps." } ]

    return render_template('index.html', posts=posts )

app.run(debug=True)



    

