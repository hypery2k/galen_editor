==============================================================
body-element		css		body
navbar-containe5	id		#navbar-absolute-top
navbar-top-*		css		.navbar-absolute-top
menubar-left		css		.sidebar-left
content-1			css		.app-content
screen-*			css		.app-content
scroll-content		css		.scrollable-content
============================================================== 

@  Overall layout  |   * 
-------------------------- 
content-1
	visible
navbar-top-*
    visible

@  Sidebar hidden on mobile |  *
-------------------------- 
menubar-left
	on bottom left: app-screen 10px left
	on top left:  navbar-top-* 0px left,  0  px bottom 

@  Content should fit to screen size on mobile  |  phone, tablet 
-------------------------- 
content-1
    width: 100% of screen/width 
    below:  navbar-top-*  0  px 
scroll-content 
    inside:  content-1  0px
     
     
@  Content use complete width on mobile  |  phone
-------------------------- 
content-1
    width:  100% of screen/width 
     
@  Content use complete width on mobile  |  tablet 
-------------------------- 
content-1
    width:  70 to 100% of screen/width 
    inside :screen  0 px  left 


@  Content use complete width on mobile  |  desktop 
-------------------------- 
content-1
    width:  70 to 100% of screen/width 
    inside: app-screen  300 to 320 px  left
