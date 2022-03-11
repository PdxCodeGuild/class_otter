from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) 
def index():
    if request.method == 'POST':
        
        user_dist = int(request.form['distance'])
        
        user_unit = request.form['in_units']
        
        user_out_unit = request.form['out_unit']

        convr_unit_m = {

            'inches': .0254,
            'feet': .3048, 
            'yards': .9144,
            'miles': 1609.34,
            'meters':  1,
            'kilometers': 1000
        }

        unit_scale = convr_unit_m[user_unit]

        unit_convr = user_dist * unit_scale

        unit_scale_out = convr_unit_m[user_out_unit]

        m_convr_out = unit_convr / unit_scale_out

        # print(m_convr_out + user_out_unit)
        
        
        return render_template('index.html', user_dist=user_dist, user_unit=user_unit, user_out_unit=user_out_unit, m_convr_out=m_convr_out)
    return render_template('index.html')

app.run(debug=True)
