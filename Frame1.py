#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNSHOWDIALOG, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATUSBAR1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(347, 270), size=wx.Size(853, 467),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Our First GUI')
        self.SetClientSize(wx.Size(853, 467))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(853, 467),
              style=wx.TAB_TRAVERSAL)

        self.btnShowDialog = wx.Button(id=wxID_FRAME1BTNSHOWDIALOG,
              label=u'Click Me', name=u'btnShowDialog', parent=self.panel1,
              pos=wx.Point(261, 145), size=wx.Size(85, 29), style=0)
        self.btnShowDialog.Bind(wx.EVT_BUTTON, self.OnBtnShowDialogButton,
              id=wxID_FRAME1BTNSHOWDIALOG)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self.panel1, style=0)
        self.statusBar1.SetHelpText(u'this is help text')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtnShowDialogButton(self, event):
        wx.MessageBox('You Clicked the button', 'Info', wx.ICON_INFORMATION)
        #event.Skip()
