"""
flask imports
import all the necessary module required for routing

"""
from flask import render_template
from . import shop



@shop.route('/shop')
def shop_page():
    """
    shopping page 
    """
    #actions here
    return render_template('shop.html')
