#Boa:Frame:FrameMain

import wx
import FrameSecond

def create(parent):
    return FrameMain(parent)

[wxID_FRAMEMAIN, wxID_FRAMEMAINBTNEXIT, wxID_FRAMEMAINBTNSHOWNEW, 
 wxID_FRAMEMAINPANEL1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class FrameMain(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEMAIN, name=u'FrameMain',
              parent=prnt, pos=wx.Point(593, 310), size=wx.Size(400, 340),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Main Frame')
        self.SetClientSize(wx.Size(400, 340))
        self.Center(wx.BOTH)

        self.panel1 = wx.Panel(id=wxID_FRAMEMAINPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(400, 340),
              style=wx.TAB_TRAVERSAL)

        self.btnShowNew = wx.Button(id=wxID_FRAMEMAINBTNSHOWNEW,
              label=u'Show the other Frame', name=u'btnShowNew',
              parent=self.panel1, pos=wx.Point(160, 63), size=wx.Size(138, 29),
              style=0)
        self.btnShowNew.Bind(wx.EVT_BUTTON, self.OnBtnShowNewButton,
              id=wxID_FRAMEMAINBTNSHOWNEW)

        self.btnExit = wx.Button(id=wxID_FRAMEMAINBTNEXIT, label=u'Exit',
              name=u'btnExit', parent=self.panel1, pos=wx.Point(160, 96),
              size=wx.Size(85, 29), style=0)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExitButton,
              id=wxID_FRAMEMAINBTNEXIT)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.FS = FrameSecond.FrameSecond(self)

    def OnBtnShowNewButton(self, event):
        #event.Skip()
        self.FS.Show()
        self.Hide()

    def OnBtnExitButton(self, event):
        #event.Skip()
        self.Close()
