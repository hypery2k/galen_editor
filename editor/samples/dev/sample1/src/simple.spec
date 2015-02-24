==========================================================
navbar-container	id		navbar
navbar-top-1		css		#navbar.navbar-absolute-top
menubar-left		css		.sidebar-left
content-*			css		.app-content
app-screen			css		.app-content
scroll-content		css		.scrollable-content
search-panel       	id      search-bar
search-panel-input	xpath   //div[@id='search-bar']/input[@type='text']
search-panel-button	css     #search-bar a
============================================================

# just a comment

navbar-top-1
	visible

^ | * 
--------------------------

navbar-top-1
	visible

@   Overall layout  | *
--------------------------
content-*
	visible

navbar-top-1
	visible


@  Content use complete width on mobile  | mobile
--------------------------
app-screen
	width: 70px
	inside: app-screen 10px

@  Content use complete width on mobile and desktop  |  mobile, desktop
--------------------------
app-screen
	width: 70px
	inside: app-screen 10px
	
	