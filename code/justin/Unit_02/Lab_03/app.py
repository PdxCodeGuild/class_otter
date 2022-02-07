from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
    {
        'title': "Partner network crowdfunding",
        'author': "Frank Careers",
        'date': "Feb 2nd, 2022",
        'body': "Long tail iPad burn rate sales traction deployment product management handshake. Termsheet client entrepreneur marketing angel investor stock graphical user interface business-to-consumer facebook. Crowdsource advisor first mover advantage supply chain non-disclosure agreement influencer success bootstrapping responsive web design freemium growth hacking social proof. Hackathon social proof direct mailing entrepreneur crowdsource ecosystem strategy long tail rockstar prototype leverage hypotheses metrics. Interaction design buzz infrastructure founders ownership bootstrapping hypotheses ecosystem A/B testing conversion graphical user interface freemium bandwidth. Crowdfunding launch party stealth interaction design research & development mass market vesting period supply chain. Prototype angel investor lean startup branding monetization infographic. Iteration return on investment android A/B testing graphical user interface. Infographic buyer user experience churn rate leverage metrics virality business-to-consumer assets hackathon alpha equity creative. Disruptive sales learning curve stealth supply chain vesting period channels."
    },
    {
        'title': "Gamification MVP",
        'author': "Leah Feralli",
        'date': "Jan 6th, 2022",
        'body': "Focus low hanging fruit bandwidth graphical user interface innovator partnership iPhone. Gamification MVP interaction design. Hackathon niche market value proposition twitter deployment stock infographic first mover advantage business-to-business partner network network effects incubator iPhone business-to-consumer. Handshake pitch infographic research & development customer innovator early adopters release entrepreneur burn rate A/B testing. Ownership equity non-disclosure agreement angel investor interaction design android scrum project buyer product management creative learning curve funding beta. Founders buzz user experience ramen seed money responsive web design startup disruptive. Holy grail partner network buzz. Customer burn rate lean startup mass market android MVP. Influencer iteration accelerator hackathon graphical user interface buzz sales beta strategy direct mailing bandwidth burn rate. Innovator prototype value proposition seed money hackathon niche market twitter leverage."
    },
    {
        'title': "Crowdsource growth hacking",
        'author': "Frank Careers",
        'date': "Dec 3rd, 2021",
        'body': "Startup direct mailing termsheet long tail MVP supply chain pitch android business-to-consumer value proposition seed money accelerator branding. Non-disclosure agreement interaction design market android user experience partnership growth hacking venture. Advisor bootstrapping traction hypotheses leverage. Bootstrapping startup branding angel investor analytics strategy launch party long tail marketing low hanging fruit accelerator. Ecosystem stock first mover advantage influencer metrics partner network innovator supply chain traction. Funding crowdsource growth hacking twitter. Launch party sales infographic deployment interaction design leverage monetization. Release monetization founders partnership android stealth technology pivot. Seed round bandwidth launch party channels leverage. Social proof release product management venture niche market interaction design alpha."
    },
    {
        'title': "Equity MVP supply chain",
        'author': "Frank Careers",
        'date': "Nov 1st, 2021",
        'body': "Venture accelerator non-disclosure agreement backing stealth user experience interaction design leverage seed money startup deployment. Angel investor return on investment holy grail focus client prototype assets disruptive analytics pivot. Focus handshake disruptive series A financing lean startup return on investment buzz ramen venture user experience infographic. Equity MVP supply chain freemium. Buzz backing business-to-consumer return on investment. Accelerator ownership research & development business-to-business virality strategy gamification investor MVP conversion traction. Deployment equity entrepreneur founders stock success low hanging fruit funding android crowdsource. Burn rate strategy monetization direct mailing long tail vesting period gen-z paradigm shift rockstar ecosystem low hanging fruit social proof. Market series A financing partnership seed round early adopters stock android. Mass market android strategy backing graphical user interface."
    }
]
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)