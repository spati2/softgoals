from __future__ import print_function, division
import sys,os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from pystar.template import Graph
__author__ = 'george'

def CSServices():
  resources = ["Service Resources", "Web Server", "Feedback Form Software", "Web Software",
                 "Strategic Blue Print", "Feedback", "Web Site Content", "Phone Library of Recorded Messages",
                 "Feedback1"]
  containers = ["CS", "Fund Development and Marketing", "Provincial government",
                "CS Technology Services", "CS Service", "Web Service", "Phone Service",
                "Counselling Management", "PHL Service", "Parents", "IT Department",
                "Web Task Force", "CS Web Services", "CS Phone Services", "PHL Phone Services",
                "PHL Web Services", "Counselling", "Kids and Youth"]
  graph = Graph.from_dot("CSServices", "pystar/graphviz/CSServices.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def OOOChatRooms():
  resources = []
  containers = ["CS Technology Services", "CS Service", "Web Service", "CS Web Services",
                "Counselling", "Counselling Employee", "Web Counselling"]
  graph = Graph.from_dot("OOOChatRooms", "pystar/graphviz/chat_room.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def CSComplex():
  resources = []
  containers = ["Parents", "CS Service", "Phone Service", "PHL Phone Services",
                "CS Technology Services", "CS Phone Services", "Community Resource",
                "Provincial government", "Web Service", "PHL Web Services",
                "Public Education Program", "CS Web Services", "Not For Profit Partners",
                "General Public", "Research Partners", "IT Department", "IT Company"]

def CSCounselling():
  containers = ["Counselling Resource Acquisition/Maintenance", "Counsellors Union",
                "Counselling Employee", "Counselling Public/Internal Relations",
                "Marketing and Fund Development", "Counselling Clinical Supervision Target",
                "Counselling Training", "Counselling Information Provider", "Parents",
                "Kids and Youth", "Counselling", "Counselling Management", "IT Department",
                "Web Counselling", "Activity Manager" ,"Phone System", "Voice Counselling"
                "Research Partners", "CS Services", "CS"]
  resources = ["Information in E-Library", "Information Binders at Stations",
               "Resources in the Library", "Tapes", "Tape Recording Technology", "Salary",
               "Counselling Workshops", "Double Headsets", "Training CDs", "Information/Resources",
               "Counselling Policies", "Web Moderator Meetings", "Counsellor Experience",
               "Caller Statistics", "Web Site Content", "Feedback"]
  graph = Graph.from_dot("CSCounselling", "pystar/graphviz/CSCounselling.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def CSCounsellingManagement():
  containers = ["CS", "Clinical Supervision", "Counselling Management", "Counselling Management Technical Encouraging",
                "Counselling Human Resource Managment", "Counselling", "CS Technology Services",
                "Counselling Scheduling", "Director Enterprise/Blue Pumpkin", "Counselling Training Management"
                "Counselling Manager", "IT Department"]
  resources = ["Counselling Resources", "Double Head Set", "Salary", "Counselling Workshops"
               ,"Counselling Policies", "Web Moderator Meetings", "Call Statistics",
               "Historical Data of Call Volumes"]
  graph = Graph.from_dot("CSCounsellingManagement", "pystar/graphviz/CSCounsellingManagement.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def CSCounsellingManagementSD():
  containers = ["CS", "Clinical Supervision", "Counselling Management", "Counselling Management Technical Encouraging",
                "Counselling Human Resource Managment", "Counselling", "CS Technology Services",
                "Counselling Scheduling", "Director Enterprise/Blue Pumpkin", "Counselling Training Management"
                "Counselling Manager", "IT Department"]
  resources = ["Counselling Resources", "Double Head Set", "Salary", "Counselling Workshops"
               ,"Counselling Policies", "Web Moderator Meetings", "Call Statistics",
               "Historical Data of Call Volumes"]
  graph = Graph.from_dot("CSCounsellingManagementSD", "pystar/graphviz/CSCounsellingManagementSD.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def CSCounsellingSD():
  containers = ["Counselling Resource Acquisition/Maintenance", "Counsellors Union",
                "Counselling Employee", "Counselling Public/Internal Relations",
                "Marketing and Fund Development", "Counselling Clinical Supervision Target",
                "Counselling Training", "Counselling Information Provider", "Parents",
                "Kids and Youth", "Counselling", "Counselling Management", "IT Department",
                "Web Counselling", "Activity Manager" ,"Phone System", "Voice Counselling"
                "Research Partners", "CS Services", "CS", "Counselling Support to Counselling"]

  resources = ["Information in E-Library", "Information Binders at Stations",
               "Resources in the Library", "Tapes", "Tape Recording Technoloyg", "Salary",
               "Counselling Workshops", "Double Headsets", "Training CDs", "Information/Resources",
               "Counselling Policies", "Web Moderator Meetings", "Counsellor Experience",
               "Caller Statistics", "Web Site Content", "Feedback"]
  graph = Graph.from_dot("CSCounsellingSD", "pystar/graphviz/CSCounsellingSD.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph

def CSFDandMarketing():
  containers = ["CS", "CS Services", "Individual donor", "SA Program", "CEO +CFO", "Not for Profit Partners",
                "VP Marketing and Fund Development", "Counselling", "Regional Offices", "IT department"]
  resources = ["Free advertisement", "Sponsor Logo", "Funds", "Agreement", "Exclusive Brand and Logo use",
               " Free services", "Sponsor partner\ncontacts", "Sponsor partner\ncontacts1", "Sponsor partner\ncontacts2",
               "Single charitable registration number", "Single charitable registration number1",
               "National Marketing Strategy ", "Sponsor Logo", "Donor/Accounting Database", "Promotion Resources"]
  graph = Graph.from_dot("CSFDandMarketing", "pystar/graphviz/CSFD and Marketing.gv", resources, containers)
  Graph.json(graph, "pystar/json/%s.json"%graph.name)
  return graph
