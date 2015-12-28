from flask import render_template, Flask, redirect, url_for, flash
from .. import main
#from .forms import AddInventoryItemForm, EditInventoryItemForm, DeleteConfirm
#from .. import db
#from ..models import Inventory, Material, Design, Piece, designs, pieces, materials

@main.route('/')
def hello_world():
    return render_template('index.html')