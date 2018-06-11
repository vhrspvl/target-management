# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "target_management_system"
app_title = "Target Management System"
app_publisher = "Frappé"
app_description = "App for allocating and monitoring employee target details"
app_icon = " octicon octicon-book"
app_color = "#589494"
app_email = "ramya.a@voltechgroup.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/target_management_system/css/target_management_system.css"
# app_include_js = "/assets/target_management_system/js/target_management_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/target_management_system/css/target_management_system.css"
# web_include_js = "/assets/target_management_system/js/target_management_system.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "target_management_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "target_management_system.install.before_install"
# after_install = "target_management_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "target_management_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"target_management_system.tasks.all"
# 	],
# 	"daily": [
# 		"target_management_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"target_management_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"target_management_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"target_management_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "target_management_system.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "target_management_system.event.get_events"
# }

