
from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')
#     return '<html><head></head><body><h1>Hello world!</h1></body></html'

@app.route('/')
def blog():

    posts = [{
        'title': 'My First Post',
        'author': 'Sana Rahmani',
        'date' : '18 Feb 2002',
        'preview': """Best Practice Consultations at No-Cost - NAVREF's BPC promotes high quality operational practices among the VA-affiliated NPCs. Through this program, NAVREF supports the cost of sending two or three specifically selected, experienced executie directors or NAVREF staff members to spend two days on-site reviewing all aspects of the NPC's management. Bi-Monthly Newsletter - NAVREF sends news items relevant to NPCs to NPC executive directors. These items are posted on the NAVREF website for NAVREF member access.
    SCRS Membership - NAVREF membership comes with SCRS membership too! SCRS offers several monthly webinar series on topics of interest to research sites."""
    },{
        'title': 'My Second Post',
        'author': 'Sana Rahmani',
        'date' : '18 Feb 2002',
        'preview': """
         Funding Resources - NAVREF offers members the unique benefit to work with a single point of contact that connects industry opportunities with VA resources.
    Advocacy - NAVREF is an active participant in advocacy efforts to secure robust funding for VA research and development. This entails lobbying for an increase in the annual appropriation for the VA medical and prosthetic research account, which is separate from VA health care appropriation. NAVREF works with House and Senate Veterans Affairs Committees to highlight research and education issues pertinent to VA.
    Affinity Program - With multiple partners, NAVREF members can enjoy the benefit of using our collective strength to access competitive insurance, retirement, human resource, and procurement plans."""
    },{
        'title': 'My Third Post',
                'author': 'Sana Rahmani',
        'date' : '18 Feb 2002',
        'preview': """VA Advantages
Central Office of Research and Development (ORD) to provide overall direction

ORD Communications Department for outreach to industry

Office of Research Oversight to ensure human subject protection compliance

Local VAMC Research Service offices and ACOS/R’s to direct actual on-site research work

New simplified CRADA agreements, IP provisions deleted

Dedicated STAR team and availability of master CRADA agreements

Long-established NPCs fully capable of properly administering CT agreements (CRADAs)


        """
    },{
        'title': 'My Fourth Post',
        'author': 'Sana Rahmani',
        'date' : '18 Feb 2002',
        'preview': """Private Grants 
Grants from the American Heart Association, American Diabetes Association, and many others continue to be very important to the NPCs and should not be overlooked

Presently they account for approximately 10 percent of revenues

Overheads granted are typically lean

Still a good opportunity for most NPCs
        """
    },{
        'title': 'My Fifth Post',
        'author': 'Sana Rahmani',
        'date' : '18 Feb 2002',
        'preview': """Federal Funds Administration
Federal funds administration, NIH, DOD, CDMRP, is presently our largest source of revenues at 69% and growing

65 of the 84 NPCs administer some Federal funds

NIH and DoD budgets are not growing much

Federal grants are increasingly competitive

Only about 10 percent of NIH grant proposals are awarded

Federal grants require careful, costly administration

Federal funders allow very lean overheads for administration

Some NPCs have eroded their capital because they have relied too heavily on Federal funds administration

A few affiliated universities insist on managing all NIH awards

CDMRP (DoD) is an especially good opportunity for us
        """
    }]

    return render_template('blog.html', posts=posts)

app.run(debug=True)