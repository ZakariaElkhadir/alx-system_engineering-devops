# Networking Fundamentals

## OSI Model

### What it is
The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers. It serves as a reference for understanding and designing networks.

### How many layers it has
The OSI model consists of seven layers, each responsible for specific tasks in the communication process. These layers, from bottom to top, are: 
1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

### How it is organized
The layers are organized in a hierarchical manner, with each layer providing specific services to the layer above it and utilizing services from the layer below it. This organization enhances modularity and facilitates interoperability between different systems.

## LAN (Local Area Network)

### Typical usage
A LAN is a network that is limited to a small geographic area, such as a single building or a campus. It is commonly used for connecting devices like computers, printers, and servers within an organization.

### Typical geographical size
LANs typically cover a small geographical area, ranging from a single room to a few kilometers. They are ideal for providing fast and reliable communication within a confined space.

## WAN (Wide Area Network)

### Typical usage
A WAN is a network that spans a larger geographic area, connecting LANs over long distances. It is often used for connecting multiple offices of a company, allowing them to communicate and share resources.

### Typical geographical size
WANs cover a wide geographical area, which can range from a city to a global scale. They utilize various technologies, including leased lines, satellites, and the Internet, to connect distant locations.

## Internet

### What is an IP address
An IP (Internet Protocol) address is a numerical label assigned to each device participating in a computer network that uses the Internet Protocol for communication. It serves two main purposes: host or network interface identification and location addressing.

### What are the 2 types of IP address
There are two types of IP addresses: IPv4 (32-bit) and IPv6 (128-bit). IPv4 is the traditional addressing system, while IPv6 was introduced to address the growing exhaustion of IPv4 addresses.

### What is localhost
"Localhost" refers to the loopback address (127.0.0.1 in IPv4), allowing a device to communicate with itself. It is commonly used for testing and troubleshooting network applications.

### What is a subnet
A subnet is a logical subdivision of an IP network, created to improve network performance and security. It involves dividing a larger network into smaller, more manageable segments.

### Why IPv6 was created
IPv6 was created to address the limitations of IPv4, primarily the exhaustion of available IP addresses. With its larger address space, IPv6 provides a solution to the growing demand for unique IP addresses.

## TCP/UDP

### What are the 2 mainly used data transfer protocols for IP
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are the two main transport layer protocols for IP-based communication.

### What is the main difference between TCP and UDP
The main difference is that TCP provides reliable, connection-oriented communication with error checking and retransmission of lost data, while UDP offers faster but less reliable, connectionless communication.

### What is a port
A port is a logical endpoint for communication, identified by a numerical value. It allows multiple applications on a single device to use network resources simultaneously.

### Memorize SSH, HTTP, and HTTPS port numbers
- SSH (Secure Shell): Port 22
- HTTP (Hypertext Transfer Protocol): Port 80
- HTTPS (Hypertext Transfer Protocol Secure): Port 443

### What tool/protocol is often used to check if a device is connected to a network
The ICMP (Internet Control Message Protocol) is commonly used, and the "ping" tool is a popular utility to check the connectivity and round-trip time to a device on a network.