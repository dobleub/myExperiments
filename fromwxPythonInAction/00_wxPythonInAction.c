/*
 * untitled.c
 * 
 * Copyright 2013 dobleub <blue.culture@live.com.mx>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include "wx/wx.h"
class MyApp: public wxApp {
virtual bool OnInit();
};
class MyFrame: public wxFrame {
public:
MyFrame(const wxString& title, const wxPoint& pos,
const wxSize& size);
void OnQuit(wxCommandEvent& event);
void OnAbout(wxCommandEvent& event);
DECLARE_EVENT_TABLE()
};
enum {
ID_Quit = 1,
ID_About,
};
BEGIN_EVENT_TABLE(MyFrame, wxFrame)
EVT_MENU(ID_Quit, MyFrame::OnQuit)
EVT_MENU(ID_About, MyFrame::OnAbout)
END_EVENT_TABLE()
IMPLEMENT_APP(MyApp)
bool MyApp::OnInit() {
MyFrame *frame = new MyFrame("Hello World", wxPoint(50,50),
wxSize(450,340));
frame->Show(TRUE);
SetTopWindow(frame);
return TRUE;
}
MyFrame::MyFrame(const wxString& title, const wxPoint& pos,
const wxSize& size)
: wxFrame((wxFrame *)NULL, -1, title, pos, size) {
wxMenu *menuFile = new wxMenu;
menuFile->Append( ID_About, "&About..." );
menuFile->AppendSeparator();
menuFile->Append( ID_Quit, "E&xit" );
wxMenuBar *menuBar = new wxMenuBar;
menuBar->Append( menuFile, "&File" );
SetMenuBar( menuBar );
CreateStatusBar();
SetStatusText( "Welcome to wxWidgets!" );
}
void MyFrame::OnQuit(wxCommandEvent& WXUNUSED(event)) {
Close(TRUE);
}
void MyFrame::OnAbout(wxCommandEvent& WXUNUSED(event)) {
wxMessageBox("This is a wxWidgets Hello world sample",
"About Hello World", wxOK | wxICON_INFORMATION, this);
}
