## Configuring IP address to Routers in Packet Tracer and configuring static routes in multiple router topology
<ul>
<li>A toplogy was created using three Router-PT and two PC's connected to two routers using copper cross-over connections and serial DCE connections<br>
<img src="https://github.com/AnusreeK-2000/CN_1BM18CS017/blob/master/week3/topology.png"/>
</li>
<li>Different default gateways were configured for both the PC's .</li>
<li>A unique IP address was configured for each PC.</li>
<li>IP address was configured for each interface using CLI</li>
<li>Pinging PC1 from PC0 gave destination host unreachable</li>
<li>ip routes for each router was viewed using the command: show ip route</li>
<li>Static ip route was configured for each router using CLI commands: ip route destination_network subnet_mask next_hop_address </li>
<img src="https://github.com/AnusreeK-2000/CN_1BM18CS017/blob/master/week3/router0.png"/>
<img src="https://github.com/AnusreeK-2000/CN_1BM18CS017/blob/master/week3/router1.png"/>
<img src="https://github.com/AnusreeK-2000/CN_1BM18CS017/blob/master/week3/router2.png"/>
<br>
<li>Pinging PC0 from PC1 and PC1 from PC0 gave the required ping responses</li>
<img src="https://github.com/AnusreeK-2000/CN_1BM18CS017/blob/master/week3/ping_pc1_from_pc0.png"/>
<img src="https://github.com/AnusreeK-2000/CN_1BM18CS017/blob/master/week3/ping_pc0_from_pc1.png"/>
</ul>

### Learning outcomes
<ul>
<li>Creating a topology with multiple routers.</li>
<li>Configuring default gateway and ip address.</li>
<li>Configuring ip address for the interfaces</li>
<li>Pinging gives destination host unreachable if the device networks are not directly connected</li>
<li>Configuring static ip routes</li>
<li>On configuring the static ip routes, pinging gives the required response</li>
</ul>
