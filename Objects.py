from TopProcessParser import *
from OutputValidator import *
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse(r"C:\Users\abed\Desktop\New folder (4)\parameters.xml").getroot()
    return root.find(".//" + node_name).text

parser_functions= p_functions()
validator_functions= v_functions()

