import gi

I = 100
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,GdkPixbuf,Gdk
from OpenGLViewer import OpenGL
from VulkanViewer import Vulkan
from About import about


class GPUViewer(Gtk.Window):
	"""docstring for GPUViewer"""
	def __init__(self):
		Gtk.Window.__init__(self,title="GPU Viewer v1.1")
		Screen = Gdk.Screen.get_default()
		if Screen.get_height() > 950 :
			self.set_size_request(1000,950)
		else:
			self.set_size_request(1000,720)
		
		self.notebook = Gtk.Notebook()
		self.add(self.notebook)

		self.tab1 = Gtk.VBox(spacing=10)
		self.tab1.set_border_width(20)
		imgOpenGL = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="../Images/OpenGL.png", width=I, height=I, preserve_aspect_ratio=True)
		self.notebook.append_page(self.tab1,Gtk.Image.new_from_pixbuf(imgOpenGL))
	
		OpenGL(self.tab1)

		self.tab2 = Gtk.VBox()
		self.tab2.set_border_width(20)
		imgVulkan = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="../Images/Vulkan.png", width=I, height=I, preserve_aspect_ratio=True)
		self.notebook.append_page(self.tab2,Gtk.Image.new_from_pixbuf(imgVulkan))

		Vulkan(self.tab2)

		self.tab3 = Gtk.VBox()
		self.tab3.set_border_width(20)
		imgAbout = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="../Images/aboutus.png", width=I, height=50, preserve_aspect_ratio=False)
		self.notebook.append_page(self.tab3,Gtk.Image.new_from_pixbuf(imgAbout))

		about(self.tab3)


win = GPUViewer()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()