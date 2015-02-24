==============================================================
navbar		      	css     .navbar-header
navbar-item-*		css     .navbar-collapse .nav li 
menubar-left        css     .sidebar-left
header             	css     .bs-docs-header
content             css     .bs-docs-container
==============================================================

@ Overall layout | *
--------------------------
content
   visible
navbar
   visible
content
   below: navbar 400 to 410 px

   	
@ navigation hidden on mobile | mobile
--------------------------
navbar-item-*
   absent


@ navigation shown on desktop | desktop
--------------------------
navbar-item-*
   visible   


@ Content should fit to screen size | mobile
--------------------------
content
   width: 100% of screen/width


@ Content should fit to screen size | desktop
--------------------------
content
   width: 80 to 90% of screen/width
    