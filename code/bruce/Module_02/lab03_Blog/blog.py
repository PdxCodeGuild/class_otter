# ********************************************************* #
#                        Lab 3: Blog                        #
#   flask responsive flexbox grid blog framework html css   #
#                        Version: 1.0                       #
#                    Author: Bruce Stull                    #
#                         2022-02-07                        #
# ********************************************************* #

# Source blog posts go here:

posts = [
    {
        'title': "Knausgaard brooklyn tacos asymmetrical",
        'author': "KnomeChompsky-TheKingOfAllChomps",
        'date': "0220-20-02",
        'id': '17',
        'body': "Knausgaard brooklyn tacos asymmetrical wolf iPhone kale chips aliquip consectetur duis kickstarter velit disrupt freegan truffaut. Small batch shabby chic yr, PBR&B tempor cold-pressed banjo chambray williamsburg waistcoat enamel pin consequat. Hella aesthetic shaman franzen cornhole, literally aliquip. Photo booth quis locavore vaporware asymmetrical, swag biodiesel cliche cornhole gluten-free."
    },
    {
        'title': "Readymade VHS sriracha mlkshk",
        'author': "GnomeChompsky",
        'date': "2002-20-02",
        'id': '13',
        'body': "Readymade VHS sriracha mlkshk bicycle rights whatever succulents cold-pressed non gochujang typewriter labore irure kitsch. Ramps tousled raw denim lumbersexual ex esse. Est polaroid lumbersexual pitchfork nisi tofu, ugh small batch celiac occaecat bushwick consectetur +1 anim edison bulb. Copper mug intelligentsia dolore labore, tumblr cupidatat kogi quis master cleanse forage. Hashtag gastropub ramps meh lorem ad ut wayfarers bitters. Seitan deep v live-edge jean shorts, exercitation hell of squid gluten-free ennui heirloom marfa. Wayfarers pour-over waistcoat yuccie, bushwick vexillologist chicharrones nisi qui in."
    },
    {
        'title': "Blue bottle chillwave unicorn",
        'author': "GnomeChompsky",
        'date': "2002-02-20",
        'id': '11',
        'body': "Blue bottle chillwave unicorn, beard locavore humblebrag cornhole lo-fi hoodie keffiyeh velit. Bicycle rights chia dolore truffaut chillwave lyft iceland shoreditch keytar kale chips. Photo booth messenger bag venmo salvia small batch lorem. Ut occaecat hell of laborum humblebrag cupidatat dolor aliquip gluten-free lyft ea bicycle rights gochujang. Mumblecore heirloom leggings jianbing nisi."
    },
    {
        'title': "Raclette marfa cred pinterest wolf",
        'author': "EdwinVanCleef",
        'date': "1001-10-01",
        'id': '7',
        'body': '''Ramen entrepreneur twitter. Interaction design infrastructure ecosystem metrics crowdfunding business plan seed money accelerator long tail direct mailing ramen creative partnership. Stealth startup rockstar. Entrepreneur analytics founders venture. Return on investment churn rate crowdfunding metrics research & development seed round ownership assets network effects low hanging fruit. Handshake stock release entrepreneur. Early adopters creative business plan prototype non-disclosure agreement MVP funding launch party interaction design entrepreneur. Low hanging fruit success prototype backing equity focus burn rate gamification hypotheses. Launch party value proposition burn rate funding crowdsource seed round startup. Leverage learning curve alpha disruptive handshake stock niche market bandwidth business model canvas customer bootstrapping launch party.
        \n
        Bandwidth iPhone value proposition funding. Growth hacking ecosystem backing network effects crowdsource beta channels alpha assets infrastructure client technology. Early adopters user experience business model canvas innovator value proposition series A financing. Vesting period gen-z research & development customer pitch iteration business-to-business success buyer incubator ownership gamification agile development influencer. Low hanging fruit ecosystem interaction design client network effects pivot hackathon seed money customer incubator. Innovator product management analytics first mover advantage user experience social proof. Ownership technology backing customer vesting period founders long tail innovator non-disclosure agreement user experience churn rate responsive web design. Crowdfunding lean startup partnership ownership partner network analytics. Holy grail market social proof creative niche market traction crowdfunding business model canvas gen-z growth hacking branding beta seed round crowdsource. Startup return on investment hackathon.'''
    },
    {
        'title': "Mumblecore typewriter occupy",
        'author': "SilvanasWindrunner",
        'date': "1001-01-10",
        'id': '5',
        'body': "Mumblecore typewriter occupy, pickled neutra echo park meh yuccie. Truffaut street art pop-up, kale chips edison bulb poke vaporware fingerstache commodo est. Palo santo fugiat plaid minim tofu. Disrupt proident taxidermy post-ironic. Salvia hoodie flexitarian hammock, ut duis 8-bit 90's cupidatat dreamcatcher."
    },
    {
        'title': "Raclette marfa cred pinterest wolf",
        'author': "EdwinVanCleef",
        'date': "3003-03-30",
        'id': '3',
        'body': '''First mover advantage success gen-z learning curve buzz seed money client pivot stock handshake return on investment. Analytics network effects mass market customer market low hanging fruit paradigm shift buzz disruptive series A financing. Innovator series A financing niche market business model canvas validation release infrastructure paradigm shift partner network partnership business-to-business. Infographic advisor stock backing android client. Deployment twitter infographic long tail innovator accelerator social proof analytics branding MVP. Ecosystem direct mailing scrum project launch party first mover advantage pitch backing. Market pivot deployment validation. Leverage infographic bandwidth sales partnership. Churn rate freemium assets iPad. Seed round founders MVP seed money launch party.
        \n
        Bandwidth freemium social proof virality holy grail funding hackathon incubator. Facebook validation stock. Conversion mass market success learning curve user experience beta business plan pitch creative investor release bandwidth. Termsheet lean startup burn rate return on investment success business plan. Client advisor twitter series A financing business-to-consumer. Learning curve hackathon social media twitter ramen focus agile development termsheet churn rate. Backing investor niche market holy grail. Investor disruptive non-disclosure agreement stock social media gen-z infrastructure client MVP validation. Funding conversion growth hacking. Investor analytics validation return on investment creative influencer.
        \n
        Seed money holy grail first mover advantage partner network founders advisor series A financing branding metrics buzz termsheet buyer marketing angel investor. Direct mailing non-disclosure agreement research & development niche market growth hacking ecosystem technology iteration rockstar vesting period crowdsource low hanging fruit. Bootstrapping handshake market. Network effects prototype incubator research & development business model canvas non-disclosure agreement. Infographic marketing stealth. Social proof channels crowdsource. Supply chain graphical user interface user experience ownership early adopters infographic influencer startup. Product management startup incubator advisor accelerator supply chain success hackathon social media non-disclosure agreement branding stock creative buyer. Accelerator seed money influencer buzz market mass market leverage user experience pivot value proposition sales. Iteration funding pitch pivot disruptive product management.'''
    },
    {
        'title': "Raclette marfa cred pinterest wolf",
        'author': "GnomeChompsky",
        'date': "0330-03-30",
        'id': '2',
        'body': "Raclette marfa cred pinterest wolf, gluten-free crucifix aesthetic meh poutine hexagon. Cornhole helvetica vaporware do woke. Cardigan et bicycle rights retro pinterest tempor, freegan vinyl twee literally unicorn art party flexitarian kale chips swag. Raclette chillwave pabst williamsburg leggings fanny pack cold-pressed, tbh hot chicken subway tile enamel pin street art nulla plaid."
    }
]