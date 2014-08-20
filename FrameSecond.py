#Boa:Frame:FrameSecond

import wx

def create(parent):
    return FrameSecond(parent)

[wxID_FRAMESECOND, wxID_FRAMESECONDBTNFSEXIT, wxID_FRAMESECONDSTHITHERE, 
] = [wx.NewId() for _init_ctrls in range(3)]

class FrameSecond(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMESECOND, name=u'FrameSecond',
              parent=prnt, pos=wx.Point(608, 395), size=wx.Size(371, 170),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Second Frame')
        self.SetClientSize(wx.Size(371, 170))
        self.Center(wx.BOTH)

        self.btnFSExit = wx.Button(id=wxID_FRAMESECONDBTNFSEXIT, label=u'Exit',
              name=u'btnFSExit', parent=self, pos=wx.Point(143, 110),
              size=wx.Size(85, 29), style=0)
        self.btnFSExit.Center(wx.HORIZONTAL)
        self.btnFSExit.Bind(wx.EVT_BUTTON, self.OnBtnFSExitButton,
              id=wxID_FRAMESECONDBTNFSEXIT)

        self.stHiThere = wx.StaticText(id=wxID_FRAMESECONDSTHITHERE,
              label=u"Hi there... I'm the Second Form!", name=u'stHiThere',
              parent=self, pos=wx.Point(15, 48), size=wx.Size(341, 23),
              style=0)
        self.stHiThere.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Sans'))
        self.stHiThere.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self.parent = parent
        self._init_ctrls(parent)

    def OnBtnFSExitButton(self, event):
        #event.Skip()
        self.parent.Show()
        self.Hide()
