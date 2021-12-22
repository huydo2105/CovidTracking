#!/usr/bin/python3
import gi

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2
from .vaccine import list


@Gtk.Template(resource_path='/org/example/App/window.ui')
class CovidtrackingWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CovidtrackingWindow'


    # For vaccine

    vaccinated_number = Gtk.Template.Child()
    vaccinated_percentage = Gtk.Template.Child()
    two_dose_number = Gtk.Template.Child()
    two_dose_percentage = Gtk.Template.Child()
    one_dose_number = Gtk.Template.Child()
    one_dose_percentage = Gtk.Template.Child()

    enough_dose_number = Gtk.Template.Child()
    progress_bar = Gtk.Template.Child()

    top_vaccinated_provinces = Gtk.Template.Child()
    least_vaccinated_provinces = Gtk.Template.Child()

    distribution = Gtk.Template.Child()
    vaccination = Gtk.Template.Child()

    vaccination_table = Gtk.Template.Child()
    # For vaccine

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.vaccinated_number.set_text(list[0]["vaccinated_population"])
        self.vaccinated_percentage.set_text(list[0]["vaccinated_percentage"])
        self.two_dose_number.set_text(list[1]["two_dose_population"])
        self.two_dose_percentage.set_text(list[1]["two_dose_percentage"])
        self.one_dose_number.set_text(list[2]["one_dose_population"])
        self.one_dose_percentage.set_text(list[2]["one_dose_percentage"])


        progress = float(list[1]["two_dose_percentage"].replace("% population",""))/100
        self.enough_dose_number.set_text("Fully vaccinated population: "+list[1]["two_dose_population"])
        self.progress_bar.set_fraction(progress)

        self.top_vaccinated_provinces.set_from_file("/home/huydq/Projects/CovidTracking/src/images/top_vaccinated_provinces.png")
        self.least_vaccinated_provinces.set_from_file("/home/huydq/Projects/CovidTracking/src/images/least_vaccinated_provinces.png")


        self.webview = WebKit2.WebView()
        uri = "https://api.ncovtrack.com/vaccine/vietnam/provinces?metric=doses_available&showTable=false&showMap=true"
        self.webview.load_uri(uri)
        self.distribution.pack_start(self.webview,True,True,0)

        self.webview1 = WebKit2.WebView()
        uri1 = "https://api.ncovtrack.com/vaccine/vietnam/provinces?metric=second_dose&showTable=false&showMap=true"
        self.webview1.load_uri(uri1)
        self.vaccination.pack_start(self.webview1,True,True,0)

        self.webview2 = WebKit2.WebView()
        uri2 = "https://api.ncovtrack.com/vaccine/vietnam/provinces?metric=second_dose&showTable=true&showMap=false"
        self.webview2.load_uri(uri2)
        # self.webview2.run_javascript_in_world('document.getElementsByClassName("text-lightMode  m-0 p-2")[0].style.display = "none" ','',None,None,None)
        self.vaccination_table.pack_start(self.webview2,True,True,0)

        self.show_all()













        
