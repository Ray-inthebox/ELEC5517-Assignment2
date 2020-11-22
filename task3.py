from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		h1=self.addHost('h1')
                h2=self.addHost('h2')
                h3=self.addHost('h3')
                h4=self.addHost('h4')
                h5=self.addHost('h5')
                h6=self.addHost('h6')
                h7=self.addHost('h7')
                h8=self.addHost('h8')
                h9=self.addHost('h9')
		s1=self.addSwitch('s1')
                s2=self.addSwitch('s2')
                s3=self.addSwitch('s3')
                s4=self.addSwitch('s4')
		self.addLink(h1,s2,cls=TCLink,bw=2,delay='5ms')
		self.addLink(h2,s2,cls=TCLink,bw=64,delay='5ms')
                self.addLink(h3,s2,cls=TCLink,bw=100,delay='10ms',loss=0.5)
                self.addLink(h4,s3,cls=TCLink,bw=32,delay='3ms')
                self.addLink(h5,s3,cls=TCLink,bw=64,delay='3ms',loss=0.5)
                self.addLink(h6,s3,cls=TCLink,bw=600,delay='3ms',loss=0.5)
                self.addLink(h7,s4,cls=TCLink,bw=2,delay='6ms')
                self.addLink(h8,s4,cls=TCLink,bw=4,delay='6ms')
                self.addLink(h9,s4,cls=TCLink,bw=64,delay='6ms')
                self.addLink(s1,s2,cls=TCLink,bw=800,delay='4ms')
                self.addLink(s1,s3,cls=TCLink,bw=800,delay='4ms')
                self.addLink(s1,s4,cls=TCLink,bw=800,delay='4ms')
topos = {'mytopo':(lambda: MyTopo())}




