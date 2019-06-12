# 链路层和局域网

## 课后习题

### R1: 如果一个乘客类比于数据报,那么什么类比于链路层帧

运输工具类比于帧,如飞机

### R2 如果网络中,所有链路都提供可靠服务,那么 TCP 可靠传输服务是否多余

如果真的一切可靠,那就没有 TCP 可靠传输服务的事情了,如果只能保证不丢失,那么 TCP 中的流量控制,拥堵控制可靠服务还是必要的.

### R7 使用人类在鸡尾酒上面的交互类比描述轮训和令牌传输协议

轮询: 询问 A,B,C 嘉宾进行对话

令牌传输协议: 鸡尾酒上有个小令牌,小令牌在每个人手上轮流传递拿到令牌才能说话,如果一个人拿到令牌不说话,就传递给下一个人.

### R8.如果局域网有很大的周长,为什么令牌环协议是低效的

因为每个节点都只有持有令牌的时候才能发送链路帧,如果周长很大,那么意味着令牌节点很多,如果其中几个节点还要传输很多帧,那效率就很低.

### R9 MAC 地址空间多大? IPv4 呢? IPv6 呢

Mac: f0:18:98:38:eb:c0 6 个字节 2^48

IPv4: 192.168.0.1 4 字节 2^32

IPv6: 2001:0000:3238:DFE1:0063:0000:0000:FEFB 8 个 16 进制 2^128 位

### R10 假设节点 A,B,C 和通过他们的适配器都在同一个局域网

如果 A 向 B 发送 IP 数据报,C 的适配器不会处理这些帧

C 只可能会丢弃这些网络帧,不会发送到网络层,如果 A 通过广播形式发送这些帧,C 处理手段是丢弃.

### R11 ARP 查询为啥要在广播帧中发送?ARP 响应为啥要在一个具有特定 MAC 地址中的帧中发送呢

ARP 查询报文中仅仅只包含源和目的 ip,还有源 MAC 地址,他不知道目的地的 ip 和 MAC 地址,所以在广播帧中发送

而 ARP 响应报文已经知道了源和目的的 IP 地址,和 Mac 地址 4 个关键信息,完全可以构建一个具有特定目的的 MAC 地址帧,不需要发送广播增加链路的负担