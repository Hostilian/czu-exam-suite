# -*- coding: utf-8 -*-
import os
import json
import re

# 64 hand-crafted exam-accurate multiple-choice questions corresponding to the 64 cards
DATABASE = [
  {
    "q": "What is the primary purpose of an Operating System, and what are the three key system resources it controls and allocates?",
    "options": [
      "Acts as a bridge between user/apps and hardware; controls CPU time, operating memory (RAM), and local storage (HDD/SSD).",
      "Performs code compilation, database querying, and network routing directly.",
      "Runs disk defragmentation, virus scanning, and system backups automatically.",
      "Manages browser cookies, session variables, and network gateways."
    ],
    "answers": [
      "Acts as a bridge between user/apps and hardware; controls CPU time, operating memory (RAM), and local storage (HDD/SSD)."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "What are the 5 core components/elements that compose a modern operating system?",
    "options": [
      "Kernel, File System, Programming Language, User Interface (UI), and API.",
      "CPU, RAM, Hard Drive, Monitor, and Keyboard.",
      "Compiler, Linker, Assembler, Debugger, and Text Editor.",
      "BIOS, Bootloader, Device Drivers, Desktop Environment, and Web Browser."
    ],
    "answers": [
      "Kernel, File System, Programming Language, User Interface (UI), and API."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "What is the key operational difference between Cooperative and Preemptive multitasking?",
    "options": [
      "Cooperative multitasking is only used in modern systems; Preemptive was used in legacy Windows 3.x.",
      "Cooperative multitasking has the OS forcibly reclaim CPU control; Preemptive relies on apps to voluntarily yield control.",
      "Cooperative multitasking relies on apps to voluntarily yield CPU control; Preemptive multitasking allows the OS to forcibly reclaim CPU control via timer interrupts.",
      "Cooperative multitasking runs tasks in parallel; Preemptive multitasking runs tasks sequentially."
    ],
    "answers": [
      "Cooperative multitasking relies on apps to voluntarily yield CPU control; Preemptive multitasking allows the OS to forcibly reclaim CPU control via timer interrupts."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "How do mobile operating systems differ in design requirements and constraints compared to desktop systems?",
    "options": [
      "Mobile OSs focus on battery optimization, touchscreen interfaces, background process restrictions, and sandboxing.",
      "Mobile OSs require more RAM and higher CPU clocks, and use CLI as their main interface.",
      "Mobile OSs do not support networking or virtual memory due to screen size limitations.",
      "Mobile OSs prioritize multi-monitor routing and physical hard disk defragmentation."
    ],
    "answers": [
      "Mobile OSs focus on battery optimization, touchscreen interfaces, background process restrictions, and sandboxing."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "Contrast Type 1 (bare-metal) and Type 2 (hosted) hypervisors. Which statement is correct?",
    "options": [
      "Type 1 hypervisors run directly on the physical hardware (e.g., VMware ESXi); Type 2 runs as an app on top of a host OS (e.g., VirtualBox).",
      "Type 1 hypervisors run as applications on top of a host OS; Type 2 hypervisors run directly on physical hardware.",
      "Type 1 hypervisors are slower because they require a host OS layer.",
      "Type 2 hypervisors are highly secure and primarily used in enterprise datacenters."
    ],
    "answers": [
      "Type 1 hypervisors run directly on the physical hardware (e.g., VMware ESXi); Type 2 runs as an app on top of a host OS (e.g., VirtualBox)."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "Explain the difference between Copyleft and Permissive open-source licenses.",
    "options": [
      "Copyleft (e.g., GPL) allows closing modified code; Permissive (e.g., MIT) forbids private redistribution.",
      "Copyleft (e.g., GPL) requires modified/derivative software to be open-source under the same license; Permissive (e.g., MIT/Apache) allows modifying and closing source code.",
      "Copyleft licenses require payment to the authors; Permissive licenses are completely free.",
      "Copyleft applies only to kernels; Permissive applies to web application frameworks."
    ],
    "answers": [
      "Copyleft (e.g., GPL) requires modified/derivative software to be open-source under the same license; Permissive (e.g., MIT/Apache) allows modifying and closing source code."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "What is the function of the BIOS software, and where is it physically stored on the computer?",
    "options": [
      "Initializes hardware during POST and loads the OS bootloader; physically stored in non-volatile EEPROM/NAND flash on motherboard.",
      "Manages process schedules and address translations; stored in physical RAM.",
      "Defragments local hard drives at startup; stored on the boot sector of the HDD/SSD.",
      "Controls screen brightness and fan speed; stored in the CPU cache."
    ],
    "answers": [
      "Initializes hardware during POST and loads the OS bootloader; physically stored in non-volatile EEPROM/NAND flash on motherboard."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "What is the Linux kernel, and was it derived from Unix code?",
    "options": [
      "Free open-source monolithic kernel written from scratch by Linus Torvalds in 1991; Unix-like but NOT derived from Unix code.",
      "Kernel derived from original Unix Bell Labs code and modified by Microsoft.",
      "Microkernel written by Steve Jobs in 1991; derived from BSD Unix.",
      "A complete operating system including GUI, compilers, and browser written in 1991."
    ],
    "answers": [
      "Free open-source monolithic kernel written from scratch by Linus Torvalds in 1991; Unix-like but NOT derived from Unix code."
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "Which of the following is NOT one of the five key characteristics of cloud computing?",
    "options": [
      "On-Demand Self-Service",
      "Broad Network Access",
      "Static Local Resource Allocation (Non-Pooling)",
      "Rapid Elasticity",
      "Measured Service"
    ],
    "answers": [
      "Static Local Resource Allocation (Non-Pooling)"
    ],
    "cat": "OS Basics & Architecture"
  },
  {
    "q": "Name the 5 states of a process lifecycle and select a valid transition.",
    "options": [
      "New, Ready, Running, Waiting, Terminated. Transition: Running -> Ready (via timer interrupt).",
      "Ready, Running, Sleeping, Stopped, Terminated. Transition: Waiting -> Running.",
      "New, Loading, Processing, Blocked, Exited. Transition: Terminated -> Ready.",
      "Start, Queue, Active, Idle, Exit. Transition: New -> Waiting."
    ],
    "answers": [
      "New, Ready, Running, Waiting, Terminated. Transition: Running -> Ready (via timer interrupt)."
    ],
    "cat": "Process Management"
  },
  {
    "q": "Compare a process and a thread in terms of resources and memory.",
    "options": [
      "A process is a lightweight unit within a thread, sharing stack spaces.",
      "A process has its own virtual address space, memory, and unique PID; a thread runs within a process and shares its memory space and PID.",
      "A thread has a unique virtual address space and PID; processes within a thread share memory.",
      "Context switching is expensive for a thread but cheap for a process."
    ],
    "answers": [
      "A process has its own virtual address space, memory, and unique PID; a thread runs within a process and shares its memory space and PID."
    ],
    "cat": "Process Management"
  },
  {
    "q": "Explain First-Come, First-Served (FCFS) CPU scheduling and define the 'Convoy Effect'.",
    "options": [
      "Preemptive scheduling; Convoy Effect is when short processes run first.",
      "Non-preemptive scheduling where CPU goes to processes in arrival order; Convoy Effect is when short processes are stuck waiting behind one long CPU-bound process.",
      "Non-preemptive scheduling; Convoy Effect is high CPU cache utilization.",
      "Preemptive scheduling where long processes starve out short ones."
    ],
    "answers": [
      "Non-preemptive scheduling where CPU goes to processes in arrival order; Convoy Effect is when short processes are stuck waiting behind one long CPU-bound process."
    ],
    "cat": "Process Management"
  },
  {
    "q": "Explain Shortest Job First (SJF) CPU scheduling and its main implementation challenge.",
    "options": [
      "SJF chooses the process with the shortest next CPU burst; main challenge is that future CPU burst duration cannot be predicted.",
      "SJF is preemptive; main challenge is context-switch overhead.",
      "SJF is mathematically inefficient and leads to high waiting times.",
      "SJF is simple to implement because it doesn't require knowing process sizes."
    ],
    "answers": [
      "SJF chooses the process with the shortest next CPU burst; main challenge is that future CPU burst duration cannot be predicted."
    ],
    "cat": "Process Management"
  },
  {
    "q": "How does the choice of time quantum (Q) in Round Robin scheduling affect system performance?",
    "options": [
      "If Q is too small, context-switch overhead is low; if Q is too large, it causes starvation.",
      "If Q is too small, it behaves like FCFS; if Q is too large, it increases context-switch overhead.",
      "If Q is too small, context-switch overhead increases; if Q is too large, it behaves like FCFS.",
      "Time quantum choice has no effect on general-purpose OS schedulers."
    ],
    "answers": [
      "If Q is too small, context-switch overhead increases; if Q is too large, it behaves like FCFS."
    ],
    "cat": "Process Management"
  },
  {
    "q": "What are the 4 conditions that must hold simultaneously for a deadlock to occur?",
    "options": [
      "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.",
      "Paging, Swapping, Thrashing, and Page Fault.",
      "FCFS, SJF, Priority, and Round Robin.",
      "Kernel, File System, Shell, and Device Drivers."
    ],
    "answers": [
      "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait."
    ],
    "cat": "Process Management"
  },
  {
    "q": "What is the Banker's Algorithm and what deadlock strategy does it represent?",
    "options": [
      "A deadlock prevention algorithm that structurally breaks circular wait.",
      "A deadlock avoidance algorithm that checks if allocating resources leaves the system in a safe state.",
      "A deadlock detection algorithm that scans memory for loops.",
      "A deadlock recovery algorithm that terminates blocked threads."
    ],
    "answers": [
      "A deadlock avoidance algorithm that checks if allocating resources leaves the system in a safe state."
    ],
    "cat": "Process Management"
  },
  {
    "q": "Which of the following is a valid method of deadlock recovery?",
    "options": [
      "Disallowing mutual exclusion in files.",
      "Forcing resource preemption or terminating one or more deadlocked processes.",
      "Using the Banker's Algorithm to check safe states.",
      "Eliminating hold-and-wait by allocating all resources at startup."
    ],
    "answers": [
      "Forcing resource preemption or terminating one or more deadlocked processes."
    ],
    "cat": "Process Management"
  },
  {
    "q": "Describe the function and principles of Virtual Memory. How does the CPU access data stored on disk?",
    "options": [
      "Compensates for RAM shortage by utilizing disk space; CPU triggers a page fault when accessing page on disk, and the OS loads it into a RAM frame.",
      "Speeds up the system by loading the entire operating system into CPU L1 cache.",
      "Allows physical RAM to access the hard disk directly without kernel mediation.",
      "Duplicates RAM blocks to prevent hardware failure."
    ],
    "answers": [
      "Compensates for RAM shortage by utilizing disk space; CPU triggers a page fault when accessing page on disk, and the OS loads it into a RAM frame."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "What is the difference between Swapping and Paging? What is the recommended swap-to-RAM ratio?",
    "options": [
      "Swapping moves fixed-size blocks; Paging moves entire processes. Ratio is 1:1.",
      "Swapping moves entire processes to disk; Paging moves fixed-size blocks (pages). Recommended ratio is 3:1.",
      "Swapping is managed by CPU; Paging is managed by user applications. Ratio is 10:1.",
      "Paging requires SSDs; Swapping works only on traditional HDDs. Ratio is 2:1."
    ],
    "answers": [
      "Swapping moves entire processes to disk; Paging moves fixed-size blocks (pages). Recommended ratio is 3:1."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "What is the Translation Lookaside Buffer (TLB) and why is it crucial?",
    "options": [
      "A page file on disk that speeds up file reads.",
      "A hardware cache inside the MMU that stores recent virtual-to-physical address translations, avoiding double memory access.",
      "A buffer in RAM that caches browser page history.",
      "A scheduling queue that orders context switches."
    ],
    "answers": [
      "A hardware cache inside the MMU that stores recent virtual-to-physical address translations, avoiding double memory access."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "Explain FIFO page replacement and define Belady's Anomaly.",
    "options": [
      "FIFO replaces the page in memory the longest; Belady's Anomaly is when allocating more frames results in more page faults.",
      "FIFO replaces the least recently used page; Belady's Anomaly is when memory thrashing occurs.",
      "FIFO replaces the page with the lowest index; Belady's Anomaly is when more frames reduce page faults.",
      "FIFO is immune to Belady's Anomaly because it is a stack-based algorithm."
    ],
    "answers": [
      "FIFO replaces the page in memory the longest; Belady's Anomaly is when allocating more frames results in more page faults."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "Explain Least Recently Used (LRU) page replacement and why it does not suffer from Belady's Anomaly.",
    "options": [
      "LRU replaces the page unaccessed for the longest time; it is a stack algorithm, meaning frames of size n are a subset of frames of size n+1.",
      "LRU requires future memory knowledge which resolves page anomalies.",
      "LRU uses a FIFO queue that automatically scales frame allocations.",
      "LRU uses a random eviction scheme that distributes faults evenly."
    ],
    "answers": [
      "LRU replaces the page unaccessed for the longest time; it is a stack algorithm, meaning frames of size n are a subset of frames of size n+1."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "What is the Optimal Page Replacement algorithm, and why is it impossible to implement?",
    "options": [
      "Replaces the page that will not be used for the longest time in the future; impossible because it requires perfect future knowledge of memory references.",
      "Replaces the oldest page; impossible because the kernel cannot track time stamps.",
      "Replaces the largest page; impossible because pages are fixed-size.",
      "Replaces the most recently used page; impossible because of context switch overhead."
    ],
    "answers": [
      "Replaces the page that will not be used for the longest time in the future; impossible because it requires perfect future knowledge of memory references."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "Contrast internal and external memory fragmentation. Which occurs in paging?",
    "options": [
      "Internal is wasted space inside allocated blocks (occurs in paging); External is non-contiguous free blocks.",
      "Internal is non-contiguous free blocks; External is wasted space inside allocated blocks (occurs in paging).",
      "Internal fragmentation occurs in segmentation; paging suffers only from external fragmentation.",
      "Paging eliminates internal fragmentation completely by compacting memory."
    ],
    "answers": [
      "Internal is wasted space inside allocated blocks (occurs in paging); External is non-contiguous free blocks."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "Define 'Thrashing' and explain how the Working Set Model prevents it.",
    "options": [
      "Thrashing is 100% CPU usage; Working Set model allocates threads to different cores.",
      "Thrashing is when the OS spends more time swapping pages in/out than executing; Working Set model runs a process only if its active pages fit in RAM.",
      "Thrashing is hard drive formatting; Working Set model restricts file access.",
      "Thrashing is when the BIOS crashes; Working Set model reboots the system."
    ],
    "answers": [
      "Thrashing is when the OS spends more time swapping pages in/out than executing; Working Set model runs a process only if its active pages fit in RAM."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "Explain the 'empty RAM is wasted RAM' philosophy in Linux memory management.",
    "options": [
      "Linux leaves RAM empty to conserve battery on mobile devices.",
      "Linux uses almost all spare RAM as buff/cache to speed up filesystem operations, dropping it instantly if programs request memory.",
      "Linux crashes if RAM utilization falls below 90% because of kernel structure.",
      "Empty RAM is physically prone to data corruption in NAND flash memory."
    ],
    "answers": [
      "Linux uses almost all spare RAM as buff/cache to speed up filesystem operations, dropping it instantly if programs request memory."
    ],
    "cat": "Memory Management"
  },
  {
    "q": "What is the mathematical reason that the largest volume size in the FAT16 file system is 4 GB?",
    "options": [
      "FAT16 uses 16-bit addressing (65,536 clusters max) and a maximum cluster size of 64 KB, giving 65,536 * 64 KB = 4 GB.",
      "FAT16 limits sector sizes to 512 bytes on all drives.",
      "The OS kernel restricts volume sizes to fit 32-bit registers.",
      "A FAT16 table can contain only 1,024 file allocation entries."
    ],
    "answers": [
      "FAT16 uses 16-bit addressing (65,536 clusters max) and a maximum cluster size of 64 KB, giving 65,536 * 64 KB = 4 GB."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "What is an inode in Linux filesystems (ext4) and does it store the filename?",
    "options": [
      "An inode stores file metadata (size, owner, permissions, block pointers) but does NOT store the filename.",
      "An inode is a text file storing the filename and file location on disk.",
      "An inode is a directory linking filenames to their file extensions.",
      "An inode stores only the filename and directories, leaving metadata in RAM."
    ],
    "answers": [
      "An inode stores file metadata (size, owner, permissions, block pointers) but does NOT store the filename."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "Explain the Host-Terminal computational model and what the network transports.",
    "options": [
      "Central mainframe processes everything; network transports only raw inputs (keystrokes) and raw outputs (screen redraws).",
      "Network transports compiled binary files to be executed on local client computers.",
      "Clients process data locally and send SQL queries to a central database.",
      "Each user computer runs a browser as a universal client."
    ],
    "answers": [
      "Central mainframe processes everything; network transports only raw inputs (keystrokes) and raw outputs (screen redraws)."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "Describe the Batch Processing model and its primary operational feature.",
    "options": [
      "Allows real-time interactive debugging of programs on terminals.",
      "Processes jobs sequentially in batches offline, with NO user interaction during execution.",
      "Distributes computational tasks across a cloud network.",
      "Hosts web applications using a universal client model."
    ],
    "answers": [
      "Processes jobs sequentially in batches offline, with NO user interaction during execution."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "Explain the Client-Server architecture and identify the 'Universal Client' in a 3-tier model.",
    "options": [
      "Universal Client is the WWW browser (web browser) rendering the UI locally while data and logic remain on servers.",
      "Universal Client is the SSH client running on port 22.",
      "Universal Client is the operating system kernel managing local RAM.",
      "Universal Client is the local file server (proxy server)."
    ],
    "answers": [
      "Universal Client is the WWW browser (web browser) rendering the UI locally while data and logic remain on servers."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "Explain why disk defragmentation is NOT considered a core function of the OS kernel.",
    "options": [
      "It is a user-space utility software rather than a kernel routine.",
      "It is performed by the motherboard BIOS at boot time.",
      "Modern kernels do not have permissions to modify disk block positions.",
      "Defragmentation is done automatically by the hard drive hardware controllers."
    ],
    "answers": [
      "It is a user-space utility software rather than a kernel routine."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "What is a server in network communication?",
    "options": [
      "A dedicated, large physical computer that cannot run user desktop programs.",
      "A role (a program or device providing services to clients) rather than a specific physical machine.",
      "A browser application running on local client hardware.",
      "A physical interface card on a switch."
    ],
    "answers": [
      "A role (a program or device providing services to clients) rather than a specific physical machine."
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "What is the name of unwanted or malicious software that operates within the autonomous agent batch model?",
    "options": [
      "Botnet",
      "Hypervisor",
      "NAT gateway",
      "DNS Resolver"
    ],
    "answers": [
      "Botnet"
    ],
    "cat": "File Systems & Sharing Models"
  },
  {
    "q": "List the 7 layers of the OSI model in order and state the PDU for Layer 2.",
    "options": [
      "Physical, Data Link, Network, Transport, Session, Presentation, Application. Layer 2 PDU: Frame.",
      "Physical, Network, Transport, Session, Presentation, Application, Security. Layer 2 PDU: Packet.",
      "Application, Presentation, Session, Transport, Network, Data Link, Physical. Layer 2 PDU: Segment.",
      "Data, Segment, Packet, Frame, Bits, Sockets, Ports. Layer 2 PDU: Bits."
    ],
    "answers": [
      "Physical, Data Link, Network, Transport, Session, Presentation, Application. Layer 2 PDU: Frame."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Compare TCP and UDP in terms of handshakes and reliability.",
    "options": [
      "TCP is connectionless and faster; UDP is connection-oriented and uses a 3-way handshake.",
      "TCP is connection-oriented (uses a 3-way handshake SYN->SYN-ACK->ACK) and reliable; UDP is connectionless and best-effort (no handshake, no ACKs).",
      "TCP uses UDP ports for data exchange; UDP has a 4-way handshake.",
      "Both TCP and UDP are connectionless but TCP guarantees packet order using ICMP."
    ],
    "answers": [
      "TCP is connection-oriented (uses a 3-way handshake SYN->SYN-ACK->ACK) and reliable; UDP is connectionless and best-effort (no handshake, no ACKs)."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Explain the DHCP DORA process and select the correct step sequence.",
    "options": [
      "Discover, Offer, Request, Acknowledge",
      "Destination, Origin, Route, Address",
      "Domain, Option, Routing, ARP",
      "Direct, Open, Request, Allocate"
    ],
    "answers": [
      "Discover, Offer, Request, Acknowledge"
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Explain the distributed nature of DNS and the direction from which DNS resolvers read domain names.",
    "options": [
      "DNS is a centralized database; resolvers read from left to right.",
      "DNS is a distributed database; resolvers read domain names from the end (right to left), starting at the root domain.",
      "DNS resides inside local routers; resolvers read names alphabetically.",
      "DNS is hosted completely on the ICANN main server; resolvers read names byte-by-byte."
    ],
    "answers": [
      "DNS is a distributed database; resolvers read domain names from the end (right to left), starting at the root domain."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "What are private IP addresses, and how do devices using them access the public internet?",
    "options": [
      "Globally unique IPs; they access the internet directly through any switch port.",
      "Reserved local IPs (RFC 1918) that are non-routable on the internet; they access the internet via Network Address Translation (NAT) at the router.",
      "Encrypted IP addresses that bypass ISP firewalls using SSH on port 22.",
      "IP addresses reserved for class D multicasting."
    ],
    "answers": [
      "Reserved local IPs (RFC 1918) that are non-routable on the internet; they access the internet via Network Address Translation (NAT) at the router."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Compare VLAN Access Ports and Trunk Ports in 802.1Q switch configurations.",
    "options": [
      "Access Ports carry traffic for multiple VLANs; Trunk Ports belong to a single VLAN.",
      "Access Ports belong to a single VLAN and connect end-user devices (untagged frames); Trunk Ports carry traffic for multiple VLANs simultaneously using 802.1Q tagging.",
      "Access Ports are encrypted; Trunk Ports are unencrypted.",
      "Access Ports are Layer 3 interfaces; Trunk Ports are Layer 1 physical cables."
    ],
    "answers": [
      "Access Ports belong to a single VLAN and connect end-user devices (untagged frames); Trunk Ports carry traffic for multiple VLANs simultaneously using 802.1Q tagging."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Contrast the MQTT and CoAP messaging protocols used in IoT.",
    "options": [
      "MQTT runs over TCP and uses a Publish-Subscribe broker architecture; CoAP runs over UDP and uses a RESTful Request-Response model.",
      "MQTT runs over UDP and is RESTful; CoAP runs over TCP and requires a central broker.",
      "MQTT is designed for web browsers; CoAP is designed for local file servers.",
      "Both protocols run over ICMP and do not use port numbers."
    ],
    "answers": [
      "MQTT runs over TCP and uses a Publish-Subscribe broker architecture; CoAP runs over UDP and uses a RESTful Request-Response model."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Which of the following is a disadvantage of wireless networks compared to wired networks?",
    "options": [
      "Lack of mobility for portable devices.",
      "Higher installation and adaptivity costs.",
      "Prone to signal degradation, security vulnerabilities, and interference on shared unlicensed bands.",
      "Inability to carry digital binary data."
    ],
    "answers": [
      "Prone to signal degradation, security vulnerabilities, and interference on shared unlicensed bands."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "How does an Ethernet switch learn MAC addresses?",
    "options": [
      "By reading the destination MAC address of incoming frames.",
      "By reading the source MAC address of incoming frames and mapping it to the receiving port in its MAC table.",
      "By querying the DNS server whenever a frame is sent.",
      "By broadcasting ARP requests to all ports at regular intervals."
    ],
    "answers": [
      "By reading the source MAC address of incoming frames and mapping it to the receiving port in its MAC table."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Explain what happens when PC1 pings PC2 for the first time on a switch.",
    "options": [
      "PC1 sends a unicast ICMP frame directly to PC2.",
      "PC1 sends an ARP broadcast (destination MAC ff:ff:ff:ff:ff:ff) which the switch floods out all ports; PC2 replies with a unicast ARP response.",
      "PC1 queries the DNS server to find PC2's MAC address.",
      "The switch blocks the frame because MAC addresses are not yet populated."
    ],
    "answers": [
      "PC1 sends an ARP broadcast (destination MAC ff:ff:ff:ff:ff:ff) which the switch floods out all ports; PC2 replies with a unicast ARP response."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "What is an IP subnet overlap/conflict error and how is it resolved?",
    "options": [
      "Occurs when two hosts have the same MAC address; resolved by changing chmod settings.",
      "Occurs when two router interfaces/subnets are assigned overlapping IP address spaces; resolved by assigning a unique subnet range to one of the networks.",
      "Occurs when DNS and DHCP ports conflict; resolved by disabling port 53.",
      "Occurs when subnet masks are not in CIDR format."
    ],
    "answers": [
      "Occurs when two router interfaces/subnets are assigned overlapping IP address spaces; resolved by assigning a unique subnet range to one of the networks."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "What four core IP parameters must be assigned to configure a network interface on a node?",
    "options": [
      "IP Address, Subnet Mask, Default Gateway, and DNS Server.",
      "MAC Address, Hostname, SSID, and Port Number.",
      "DHCP lease, NAT rule, SSH key, and HTML content.",
      "CPU clock, RAM size, HDD storage, and OS kernel version."
    ],
    "answers": [
      "IP Address, Subnet Mask, Default Gateway, and DNS Server."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "Why do we use higher wireless frequencies (e.g., 5 GHz) despite shorter range and poorer obstacle penetration?",
    "options": [
      "They are licensed bands and therefore more secure.",
      "They offer more network bandwidth.",
      "They consume significantly less battery power.",
      "They do not require antennas to propagate."
    ],
    "answers": [
      "They offer more network bandwidth."
    ],
    "cat": "Computer Networks"
  },
  {
    "q": "What are the primary technical advantages and disadvantages of a Command Line Interface (CLI) compared to a GUI?",
    "options": [
      "Advantage: Remote access requires very low network bandwidth. Disadvantage: Steep learning curve.",
      "Advantage: Visually rich. Disadvantage: Requires high CPU and RAM.",
      "Advantage: typos are ignored. Disadvantage: slow speed.",
      "Advantage: runs only on mainframes. Disadvantage: low security."
    ],
    "answers": [
      "Advantage: Remote access requires very low network bandwidth. Disadvantage: Steep learning curve."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "What protocol does the PING diagnostic tool use, and is it available on Windows/Linux?",
    "options": [
      "Uses TCP on port 80; installed by default on Windows only.",
      "Uses UDP on port 53; installed by default on Linux only.",
      "Uses ICMP (Internet Control Message Protocol) Echo Request/Reply; installed by default on both Windows and Linux.",
      "Uses SSH on port 22; available on Linux only."
    ],
    "answers": [
      "Uses ICMP (Internet Control Message Protocol) Echo Request/Reply; installed by default on both Windows and Linux."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "How does traceroute function to map a network path?",
    "options": [
      "Sends packets with increasing TTL (Time to Live) values starting at 1. Routers discard packets at TTL=0 and send ICMP Time Exceeded messages.",
      "Performs a WHOIS query for each hop along the path.",
      "Queries the DNS server canonical CNAME records sequentially.",
      "Uses switch port mirroring to capture frames at each interface."
    ],
    "answers": [
      "Sends packets with increasing TTL (Time to Live) values starting at 1. Routers discard packets at TTL=0 and send ICMP Time Exceeded messages."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "Which Linux command is used to forcefully terminate a process (sending SIGKILL)?",
    "options": [
      "kill -15 PID",
      "kill -9 PID",
      "ps aux",
      "top -k"
    ],
    "answers": [
      "kill -9 PID"
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "Which Linux command displays free and used disk space on mounted filesystems in a human-readable format?",
    "options": [
      "df -h",
      "du -sh",
      "ls -la",
      "free -m"
    ],
    "answers": [
      "df -h"
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "In Linux, what permissions are set on a file by the command `chmod 755`?",
    "options": [
      "Owner: read/write; Group: execute; Others: none",
      "Owner: read/write/execute; Group: read/execute; Others: read/execute",
      "Owner: read/write; Group: read; Others: read",
      "Owner: read/execute; Group: read/execute; Others: none"
    ],
    "answers": [
      "Owner: read/write/execute; Group: read/execute; Others: read/execute"
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "What does the Linux command `w` show, and who is the user `vokoun`?",
    "options": [
      "Shows system uptime, load averages, and details of logged-in users; vokoun is the course instructor for ETE2AE.",
      "Shows directory listings; vokoun is the root superuser.",
      "Shows network interfaces; vokoun is the DNS server hostname.",
      "Shows swap memory statistics; vokoun is the name of the Linux kernel creator."
    ],
    "answers": [
      "Shows system uptime, load averages, and details of logged-in users; vokoun is the course instructor for ETE2AE."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "Explain how command pipelines work in Linux, and walk through the command chain: `cat file | grep 'pat' | cut -d ';' -f 6`.",
    "options": [
      "Runs commands in background; cut extracts fields.",
      "Pipes output of first command as input of second; in the chain, cat outputs the file, grep filters for the pattern, and cut extracts the 6th field.",
      "Redirects errors to a text file; cat prints and grep writes to disk.",
      "Combines standard output and standard error into a single variable."
    ],
    "answers": [
      "Pipes output of first command as input of second; in the chain, cat outputs the file, grep filters for the pattern, and cut extracts the 6th field."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "Why is SSH preferred over Telnet/Terminal connections?",
    "options": [
      "SSH encrypts the entire channel (usually Port 22), protecting credentials from packet sniffing; Telnet transmits in plaintext.",
      "SSH does not require a user account or password.",
      "SSH runs over UDP which makes it much faster.",
      "SSH operates at the physical layer of the OSI model."
    ],
    "answers": [
      "SSH encrypts the entire channel (usually Port 22), protecting credentials from packet sniffing; Telnet transmits in plaintext."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "What is a CNAME record in DNS, and what command finds the true server name of www.pef.czu.cz?",
    "options": [
      "Maps host to IPv4; command is nslookup.",
      "An alias mapping one domain to another (canonical name); command is `dig www.pef.czu.cz CNAME`, which returns `wlbnginx.czu.cz`.",
      "A mail server record; command is whois.",
      "A reverse lookup pointer; command is ping."
    ],
    "answers": [
      "An alias mapping one domain to another (canonical name); command is `dig www.pef.czu.cz CNAME`, which returns `wlbnginx.czu.cz`."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "What is the function of the WHOIS utility, and what organization owns the IP 94.199.40.226?",
    "options": [
      "Queries registration databases for owner details; IP 94.199.40.226 is owned by Ministerstvo vnitra CR (Ministry of the Interior of the Czech Republic).",
      "Configures router access control lists; owned by CZU Prague.",
      "Monitors CPU loads remotely; owned by Seznam.cz.",
      "Performs active port scans; owned by Google LLC."
    ],
    "answers": [
      "Queries registration databases for owner details; IP 94.199.40.226 is owned by Ministerstvo vnitra CR (Ministry of the Interior of the Czech Republic)."
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "How do you customize the packet payload size to 1400 bytes in ping on Windows vs Linux?",
    "options": [
      "Windows: ping -l 1400; Linux: ping -s 1400",
      "Windows: ping -s 1400; Linux: ping -l 1400",
      "Windows: ping -size 1400; Linux: ping -p 1400",
      "Windows: ping -bytes 1400; Linux: ping -payload 1400"
    ],
    "answers": [
      "Windows: ping -l 1400; Linux: ping -s 1400"
    ],
    "cat": "CLI & Diagnostics"
  },
  {
    "q": "Given processes P1 (arrival 0, burst 6), P2 (arrival 1, burst 4), P3 (arrival 2, burst 2). Under non-preemptive SJF (Shortest Job First) scheduling, what is the execution sequence?",
    "options": [
      "P1 (0-6) -> P2 (6-10) -> P3 (10-12). Avg WT = 4.33 ms.",
      "P1 (0-6) -> P3 (6-8) -> P2 (8-12). Avg WT = 3.67 ms.",
      "P2 (0-4) -> P3 (4-6) -> P1 (6-12). Avg WT = 5.00 ms.",
      "P1 (0-2) -> P2 (2-6) -> P3 (6-8). Avg WT = 2.33 ms."
    ],
    "answers": [
      "P1 (0-6) -> P3 (6-8) -> P2 (8-12). Avg WT = 3.67 ms."
    ],
    "cat": "Step-by-Step Calculations"
  },
  {
    "q": "For the host IP address 192.168.10.138/26, what are the Network Address, Broadcast Address, and number of Usable Hosts?",
    "options": [
      "Network: 192.168.10.128; Broadcast: 192.168.10.191; Usable Hosts: 62.",
      "Network: 192.168.10.0; Broadcast: 192.168.10.63; Usable Hosts: 62.",
      "Network: 192.168.10.138; Broadcast: 192.168.10.255; Usable Hosts: 254.",
      "Network: 192.168.10.128; Broadcast: 192.168.10.192; Usable Hosts: 64."
    ],
    "answers": [
      "Network: 192.168.10.128; Broadcast: 192.168.10.191; Usable Hosts: 62."
    ],
    "cat": "Step-by-Step Calculations"
  },
  {
    "q": "Given reference string: 7, 0, 1, 2, 0, 3 with 3 memory frames. How many page faults occur under FIFO page replacement?",
    "options": [
      "3 page faults",
      "4 page faults",
      "5 page faults",
      "6 page faults"
    ],
    "answers": [
      "5 page faults"
    ],
    "cat": "Step-by-Step Calculations"
  },
  {
    "q": "Describe the fields and size of an 802.1Q VLAN tag inserted into an Ethernet frame.",
    "options": [
      "Adds 4 bytes: TPID (2 bytes, 0x8100) and TCI (2 bytes, split into PCP 3 bits, DEI 1 bit, VID 12 bits).",
      "Adds 2 bytes: MAC source address and EtherType.",
      "Adds 8 bytes: IP header fields and port numbers.",
      "Adds 12 bits: VLAN identifier only."
    ],
    "answers": [
      "Adds 4 bytes: TPID (2 bytes, 0x8100) and TCI (2 bytes, split into PCP 3 bits, DEI 1 bit, VID 12 bits)."
    ],
    "cat": "Step-by-Step Calculations"
  },
  {
    "q": "What is the binary representation of the decimal number 172?",
    "options": [
      "10101100",
      "11001010",
      "10011101",
      "11110000"
    ],
    "answers": [
      "10101100"
    ],
    "cat": "Step-by-Step Calculations"
  }
]

# Write out the interactive HTML file
def generate_html():
    # Read the raw Anki TSV file if it exists, otherwise use empty string
    anki_tsv_content = ""
    anki_path = "d:/CZUU/OS_EXAM_SUITE/anki_decks/OSCN_Anki_Deck.txt"
    if os.path.exists(anki_path):
        with open(anki_path, 'r', encoding='utf-8') as f:
            anki_tsv_content = f.read()

    # Re-structure cards for Checklist and Flashcard views
    # Categories mapped to short labels in index.html
    # We will build the page content with replacement blocks
    
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🚀 OS &amp; NET Master Exam Suite | ETE2AE CZU Prague</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    /* ─── BASE DESIGN SYSTEM ──────────────────────── */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --bg: #030610;
      --surface: #090d1e;
      --surface-hover: #121832;
      --surface-glass: rgba(9, 13, 30, 0.75);
      
      --accent: #f97316;        /* Neon Orange */
      --accent-rgb: 249, 115, 22;
      --accent-glow: rgba(249, 115, 22, 0.25);
      
      --accent2: #22d3ee;       /* Bright Cyan */
      --accent2-rgb: 34, 211, 238;
      --accent2-glow: rgba(34, 211, 238, 0.25);
      
      --violet: #a78bfa;        /* Light Violet */
      --violet-glow: rgba(167, 139, 250, 0.2);
      
      --yellow: #fbbf24;        /* Gold Yellow */
      --red: #f87171;           /* Coral Red */
      --green: #4ade80;         /* Emerald Green */
      
      --text: #eef0f8;          /* Light slate text */
      --text-muted: #8b90a8;    /* Muted label text */
      --border: rgba(34, 211, 238, 0.12);
      --border-light: rgba(255, 255, 255, 0.05);
      
      --font: 'Outfit', sans-serif;
      --mono: 'JetBrains Mono', monospace;
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      --radius: 20px;
      --radius-sm: 12px;
      --radius-xs: 8px;
    }

    html {
      scroll-behavior: smooth;
      background: var(--bg);
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
    }

    /* ─── DYNAMIC MESH BACKGROUND ─────────────────── */
    .mesh-bg {
      position: fixed;
      inset: 0;
      z-index: 0;
      pointer-events: none;
      overflow: hidden;
    }
    .mesh-bg::before {
      content: '';
      position: absolute;
      width: 900px; height: 900px;
      top: -200px; left: -200px;
      background: radial-gradient(circle, rgba(var(--accent2-rgb), 0.08) 0%, transparent 70%);
      animation: drift1 25s ease-in-out infinite alternate;
    }
    .mesh-bg::after {
      content: '';
      position: absolute;
      width: 750px; height: 750px;
      bottom: -150px; right: -150px;
      background: radial-gradient(circle, rgba(var(--accent-rgb), 0.06) 0%, transparent 70%);
      animation: drift2 20s ease-in-out infinite alternate;
    }
    @keyframes drift1 {
      0% { transform: translate(0, 0) scale(1); }
      100% { transform: translate(120px, 80px) scale(1.15); }
    }
    @keyframes drift2 {
      0% { transform: translate(0, 0) scale(1); }
      100% { transform: translate(-100px, -120px) scale(1.2); }
    }

    /* ─── SCROLLBARS ──────────────────────────────── */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(0, 0, 0, 0.2);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(var(--accent2-rgb), 0.2);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(var(--accent2-rgb), 0.4);
    }

    /* ─── HEADER & NAVIGATION ─────────────────────── */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(3, 6, 16, 0.85);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--border);
      padding: 0 2rem;
    }
    .header-inner {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 70px;
      gap: 1rem;
    }
    .logo-container {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      text-decoration: none;
    }
    .logo-badge {
      font-size: 1.6rem;
      animation: pulse 3s infinite alternate;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      100% { transform: scale(1.08); filter: drop-shadow(0 0 8px var(--accent2-glow)); }
    }
    .logo-text {
      font-size: 1.25rem;
      font-weight: 900;
      letter-spacing: -0.5px;
      color: var(--text);
    }
    .logo-text span {
      background: linear-gradient(135deg, var(--accent2), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .syllabus-code {
      background: rgba(var(--accent2-rgb), 0.12);
      border: 1px solid rgba(var(--accent2-rgb), 0.35);
      color: var(--accent2);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      padding: 2px 8px;
      border-radius: 999px;
      margin-left: 0.25rem;
    }

    nav.main-nav {
      display: flex;
      gap: 0.25rem;
    }
    .nav-btn {
      padding: 6px 14px;
      border-radius: 999px;
      font-family: var(--font);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      background: transparent;
      color: var(--text-muted);
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 0.35rem;
      white-space: nowrap;
    }
    .nav-btn:hover {
      color: var(--text);
      background: rgba(255, 255, 255, 0.03);
    }
    .nav-btn.active {
      background: linear-gradient(135deg, rgba(var(--accent2-rgb), 0.15), rgba(var(--accent2-rgb), 0.05));
      border-color: rgba(var(--accent2-rgb), 0.35);
      color: var(--accent2);
      box-shadow: 0 0 15px rgba(var(--accent2-rgb), 0.1);
    }
    .offline-badge {
      display: flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--green);
      background: rgba(74, 222, 128, 0.08);
      border: 1px solid rgba(74, 222, 128, 0.2);
      padding: 4px 10px;
      border-radius: 999px;
      white-space: nowrap;
    }
    .offline-dot {
      width: 6px;
      height: 6px;
      background-color: var(--green);
      border-radius: 50%;
      box-shadow: 0 0 6px rgba(74, 222, 128, 0.5);
      animation: blink 1.5s infinite alternate;
    }
    @keyframes blink {
      0% { opacity: 0.3; }
      100% { opacity: 1; }
    }

    /* ─── MAIN CONTAINER ──────────────────────────── */
    main {
      position: relative;
      z-index: 1;
      max-width: 1400px;
      margin: 0 auto;
      padding: 1.5rem 1.5rem 4rem;
    }

    /* ─── GLASS PANEL CLASS ───────────────────────── */
    .glass-panel {
      background: var(--surface-glass);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border-light);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .glass-panel.glowing {
      border-color: rgba(var(--accent2-rgb), 0.15);
    }

    /* ─── TIMERS & STATISTICS HERO ────────────────── */
    .hero-stats-panel {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }
    @media (max-width: 900px) {
      .hero-stats-panel {
        grid-template-columns: 1fr;
      }
    }

    .time-tracker-box {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      background: linear-gradient(135deg, rgba(var(--accent-rgb), 0.08), rgba(var(--accent2-rgb), 0.04));
      border: 1px solid rgba(var(--accent-rgb), 0.2);
    }
    .timer-circle {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: rgba(249, 115, 22, 0.1);
      border: 2px dashed var(--accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      animation: spin 30s linear infinite;
    }
    @keyframes spin {
      100% { transform: rotate(360deg); }
    }
    .timer-info h3 {
      font-size: 1.6rem;
      font-family: var(--mono);
      font-weight: 800;
      color: var(--accent);
      line-height: 1.1;
    }
    .timer-info p {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .stats-card-box {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }
    .stats-donut-container {
      position: relative;
      width: 60px;
      height: 60px;
      flex-shrink: 0;
    }
    .stats-donut-label {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 800;
      font-family: var(--mono);
      color: var(--text);
    }
    .stats-card-details h4 {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .stats-card-details p {
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.2;
    }

    /* ─── ACTIVE RECALL PINK BLURS ────────────────── */
    .blur-reveal {
      filter: blur(5px);
      background-color: rgba(244, 63, 94, 0.18);
      border-radius: 4px;
      padding: 0 4px;
      cursor: pointer;
      transition: filter 0.25s ease, background-color 0.25s ease;
      user-select: none;
    }
    .blur-reveal:hover, .blur-reveal.revealed {
      filter: blur(0);
      background-color: transparent;
    }

    /* ─── PANELS VIEW CONTROL ─────────────────────── */
    .view-pane {
      display: none;
      animation: fadeUp 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .view-pane.active {
      display: block;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ─── PANE 1: CHECKLIST ──────────────────────── */
    .checklist-controls {
      display: flex;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }
    .search-bar-wrap {
      flex: 1;
      min-width: 280px;
      position: relative;
    }
    .search-input {
      width: 100%;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 14px 10px 38px;
      font-family: inherit;
      font-size: 0.85rem;
      color: var(--text);
      outline: none;
      transition: var(--transition);
    }
    .search-input:focus {
      border-color: var(--accent2);
      box-shadow: 0 0 12px var(--accent2-glow);
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.9rem;
      color: var(--text-muted);
    }
    .filter-tags {
      display: flex;
      gap: 0.35rem;
      flex-wrap: wrap;
    }
    .filter-btn {
      padding: 5px 12px;
      border-radius: 6px;
      background: var(--surface);
      border: 1px solid var(--border-light);
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.78rem;
      font-weight: 600;
      transition: var(--transition);
    }
    .filter-btn:hover {
      color: var(--text);
      border-color: var(--border);
    }
    .filter-btn.active {
      background: rgba(var(--accent2-rgb), 0.12);
      border-color: var(--accent2);
      color: var(--accent2);
    }

    /* CHECKLIST ITEMS */
    .checklist-grid {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
    }
    .q-item-card {
      background: rgba(12, 15, 30, 0.45);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
      overflow: hidden;
      transition: var(--transition);
    }
    .q-item-card:hover {
      border-color: rgba(var(--accent2-rgb), 0.25);
      background: rgba(12, 15, 30, 0.7);
    }
    .q-item-card.mastered {
      border-color: rgba(74, 222, 128, 0.25);
      background: rgba(74, 222, 128, 0.02);
    }
    .q-item-card.needs-review {
      border-color: rgba(249, 115, 22, 0.25);
      background: rgba(249, 115, 22, 0.02);
    }
    .q-summary-row {
      display: flex;
      align-items: center;
      padding: 0.88rem 1.25rem;
      cursor: pointer;
      gap: 1rem;
      user-select: none;
    }
    .q-mastery-btns {
      display: flex;
      gap: 4px;
      flex-shrink: 0;
    }
    .q-mastery-btns button {
      width: 24px;
      height: 24px;
      border-radius: 5px;
      border: 1px solid var(--border-light);
      background: rgba(255, 255, 255, 0.02);
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.72rem;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
      font-family: var(--font);
    }
    .q-mastery-btns button:hover {
      color: var(--text);
      border-color: var(--border);
    }
    .q-mastery-btns button.check.active {
      background: rgba(74, 222, 128, 0.15);
      border-color: var(--green);
      color: var(--green);
      font-weight: bold;
    }
    .q-mastery-btns button.star.active {
      background: rgba(249, 115, 22, 0.15);
      border-color: var(--accent);
      color: var(--accent);
    }
    .q-title-wrap {
      flex: 1;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .q-badge {
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.65rem;
      font-weight: 700;
      font-family: var(--mono);
      background: rgba(255,255,255,0.05);
      color: var(--text-muted);
    }
    .q-title-text {
      font-size: 0.88rem;
      font-weight: 700;
    }
    .q-arrow {
      font-size: 0.75rem;
      color: var(--text-muted);
      transition: transform 0.25s;
    }
    .q-item-card.expanded .q-arrow {
      transform: rotate(180deg);
    }

    .q-details-row {
      display: none;
      padding: 0 1.25rem 1.25rem 3.5rem;
      border-top: 1px solid rgba(255, 255, 255, 0.02);
      animation: fadeIn 0.2s ease-out;
    }
    .q-item-card.expanded .q-details-row {
      display: block;
    }
    @keyframes fadeIn {
      from { opacity: 0; } to { opacity: 1; }
    }
    .q-desc-box {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }
    .q-ans-box {
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-xs);
      padding: 0.75rem 1rem;
      font-size: 0.85rem;
      line-height: 1.6;
    }

    /* ─── PANE 2: FLASHCARDS ─────────────────────── */
    .flashcard-stage {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 1rem 0;
    }
    .fc-box-wrap {
      width: 100%;
      max-width: 620px;
      perspective: 1400px;
      cursor: pointer;
    }
    .fc-card-body {
      position: relative;
      width: 100%;
      height: 300px;
      transform-style: preserve-3d;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .fc-card-body.flipped {
      transform: rotateY(180deg);
    }
    .fc-card-face {
      position: absolute;
      inset: 0;
      border-radius: var(--radius);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      text-align: center;
    }
    .fc-card-front {
      background: linear-gradient(135deg, rgba(9, 13, 30, 0.98), rgba(21, 27, 48, 0.92));
      border: 1px solid rgba(var(--accent2-rgb), 0.2);
      box-shadow: 0 0 40px rgba(var(--accent2-rgb), 0.05), inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .fc-card-back {
      background: linear-gradient(135deg, rgba(21, 27, 48, 0.98), rgba(9, 13, 30, 0.92));
      border: 1px solid rgba(var(--accent-rgb), 0.2);
      box-shadow: 0 0 40px rgba(var(--accent-rgb), 0.05);
      transform: rotateY(180deg);
    }
    .fc-card-cat {
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent2);
      margin-bottom: 0.75rem;
    }
    .fc-card-q {
      font-size: 1.15rem;
      font-weight: 700;
      line-height: 1.45;
      color: var(--text);
    }
    .fc-card-tap-hint {
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 1.25rem;
    }
    .fc-card-ans {
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--text);
      text-align: left;
    }

    .fc-progress-bar-wrap {
      width: 100%;
      max-width: 620px;
      height: 5px;
      background: var(--surface);
      border-radius: 99px;
      overflow: hidden;
      margin-bottom: 0.88rem;
    }
    .fc-progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent2), var(--accent));
      width: 0%;
      transition: width 0.4s ease;
    }
    .fc-stats-panel {
      display: flex;
      gap: 1.5rem;
      font-size: 0.78rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      color: var(--text-muted);
    }
    .fc-stat-item span {
      color: var(--text);
      font-family: var(--mono);
    }
    .fc-controls-row {
      display: flex;
      gap: 0.65rem;
      margin-top: 1.5rem;
      flex-wrap: wrap;
      justify-content: center;
    }
    .fc-btn {
      padding: 9px 20px;
      border-radius: 50px;
      border: 1px solid var(--border-light);
      font-family: inherit;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      background: var(--surface);
      color: var(--text);
      transition: var(--transition);
    }
    .fc-btn:hover {
      border-color: var(--border);
      transform: translateY(-1px);
    }
    .fc-btn.primary {
      background: linear-gradient(135deg, var(--accent2), var(--accent2-dim));
      color: #000;
      border: none;
      box-shadow: 0 0 15px var(--accent2-glow);
    }
    .fc-btn.primary:hover {
      box-shadow: 0 0 25px var(--accent2);
    }
    .fc-btn.bad {
      background: rgba(248, 113, 113, 0.1);
      color: var(--red);
      border-color: rgba(248, 113, 113, 0.25);
    }
    .fc-btn.bad:hover {
      background: rgba(248, 113, 113, 0.2);
    }
    .fc-btn.good {
      background: rgba(74, 222, 128, 0.1);
      color: var(--green);
      border-color: rgba(74, 222, 128, 0.25);
    }
    .fc-btn.good:hover {
      background: rgba(74, 222, 128, 0.2);
    }
    .fc-shortcuts {
      margin-top: 1rem;
      font-size: 0.65rem;
      color: var(--text-muted);
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      justify-content: center;
    }
    .fc-shortcuts kbd {
      background: var(--surface);
      border: 1px solid var(--border-light);
      border-radius: 4px;
      padding: 1px 5px;
      font-family: var(--mono);
      font-size: 0.62rem;
      color: var(--text-dim);
    }

    /* ─── PANE 3: MEMORIZE ───────────────────────── */
    .memorize-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(330px, 1fr));
      gap: 1.25rem;
    }
    .memorize-card {
      background: rgba(12, 16, 32, 0.7);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.4rem;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      transition: all 0.25s;
    }
    .memorize-card:hover {
      border-color: rgba(var(--accent2-rgb), 0.25);
      box-shadow: 0 8px 32px rgba(var(--accent2-rgb), 0.06);
    }
    .memorize-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.88rem;
    }
    .memorize-card-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent2);
    }
    .memorize-card-badge {
      font-size: 0.68rem;
      font-weight: 700;
      font-family: var(--mono);
      background: rgba(34, 211, 238, 0.1);
      color: var(--accent2);
      padding: 2px 7px;
      border-radius: 4px;
    }
    .memorize-content-group h4 {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin: 0.75rem 0 0.35rem 0;
    }
    .memorize-content-group ul {
      list-style-type: none;
      padding-left: 0.5rem;
    }
    .memorize-content-group li {
      font-size: 0.8rem;
      line-height: 1.5;
      margin-bottom: 0.4rem;
      position: relative;
      padding-left: 0.75rem;
    }
    .memorize-content-group li::before {
      content: '•';
      color: var(--accent2);
      position: absolute;
      left: 0;
    }
    .memorize-card-trap {
      margin-top: 0.88rem;
      background: rgba(249, 115, 22, 0.08);
      border: 1px solid rgba(249, 115, 22, 0.2);
      border-radius: var(--radius-xs);
      padding: 0.6rem 0.8rem;
      font-size: 0.78rem;
      line-height: 1.45;
    }

    /* ─── PANE 4: MOCK EXAM ──────────────────────── */
    .exam-start-panel {
      text-align: center;
      max-width: 580px;
      margin: 2rem auto;
    }
    .exam-icon {
      font-size: 3rem;
      margin-bottom: 1rem;
    }
    .exam-btn {
      padding: 12px 32px;
      border-radius: 50px;
      border: none;
      font-family: inherit;
      font-weight: 800;
      font-size: 0.95rem;
      cursor: pointer;
      background: linear-gradient(135deg, var(--accent2), var(--accent));
      color: #000;
      box-shadow: 0 0 20px rgba(var(--accent2-rgb), 0.2);
      transition: var(--transition);
    }
    .exam-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 30px var(--accent2);
    }
    .exam-run-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1rem;
      margin-bottom: 1rem;
    }
    .exam-timer {
      font-family: var(--mono);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--accent);
      background: rgba(249, 115, 22, 0.08);
      border: 1px solid rgba(249, 115, 22, 0.2);
      padding: 4px 12px;
      border-radius: 50px;
    }
    .exam-tracker {
      display: flex;
      gap: 4px;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
      justify-content: center;
    }
    .tracker-dot {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      border: 1px solid var(--border-light);
      background: var(--surface);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.65rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
      font-family: var(--mono);
      color: var(--text-muted);
    }
    .tracker-dot.active {
      border-color: var(--accent2);
      color: var(--accent2);
      box-shadow: 0 0 8px var(--accent2-glow);
    }
    .tracker-dot.answered {
      background: rgba(var(--accent2-rgb), 0.12);
      border-color: var(--accent2);
      color: var(--accent2);
    }
    .exam-q-box {
      margin-bottom: 2rem;
      min-height: 180px;
    }
    .exam-q-title {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      gap: 0.88rem;
    }
    .exam-q-num {
      background: rgba(var(--accent2-rgb), 0.12);
      color: var(--accent2);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-family: var(--mono);
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .exam-opts {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      padding-left: 2.8rem;
    }
    .exam-opt {
      padding: 0.88rem 1.25rem;
      border-radius: var(--radius-sm);
      background: var(--surface);
      border: 1px solid var(--border-light);
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.88rem;
      user-select: none;
    }
    .exam-opt:hover {
      border-color: var(--border);
      background: var(--surface-hover);
    }
    .exam-opt.selected {
      border-color: var(--accent2);
      background: rgba(var(--accent2-rgb), 0.08);
    }
    .exam-radio-box, .exam-check-box {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      border: 2px solid var(--text-muted);
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
    }
    .exam-check-box {
      border-radius: 4px;
    }
    .exam-opt.selected .exam-radio-box, .exam-opt.selected .exam-check-box {
      border-color: var(--accent2);
      background-color: var(--accent2);
    }
    .exam-opt.selected .exam-radio-box::after {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background-color: #000;
    }
    .exam-nav-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border);
      padding-top: 1.25rem;
    }

    /* EXAM RESULTS */
    .results-donut-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      border-right: 1px solid var(--border-light);
    }
    .results-score-circle {
      position: relative;
      width: 140px;
      height: 140px;
      margin-bottom: 1rem;
    }
    .score-circle-text {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .score-circle-text span {
      font-size: 1.8rem;
      font-weight: 900;
      line-height: 1.1;
      font-family: var(--mono);
    }
    .score-circle-text .score-circle-label {
      font-size: 0.88rem;
      color: var(--text-muted);
      font-weight: 700;
    }
    .results-outcome {
      font-size: 1.25rem;
      font-weight: 900;
      letter-spacing: 0.05em;
    }
    .results-outcome.pass { color: var(--green); }
    .results-outcome.fail { color: var(--red); }
    .results-diag-box {
      padding: 1rem;
    }
    .diag-title {
      font-size: 0.82rem;
      text-transform: uppercase;
      color: var(--text-muted);
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
    }
    .diag-bars {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .diag-bar-row {
      display: flex;
      align-items: center;
      gap: 1rem;
      font-size: 0.78rem;
    }
    .diag-bar-label {
      width: 160px;
      color: var(--text);
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .diag-bar-track {
      flex: 1;
      height: 6px;
      background: var(--surface);
      border-radius: 10px;
      overflow: hidden;
    }
    .diag-bar-fill {
      height: 100%;
      background: var(--accent2);
      border-radius: 10px;
    }
    .diag-bar-val {
      width: 40px;
      text-align: right;
      font-family: var(--mono);
      font-weight: 700;
    }
    .results-review-title {
      font-size: 1.1rem;
      font-weight: 800;
      margin: 2.5rem 0 1rem 0;
      border-left: 3px solid var(--accent);
      padding-left: 0.75rem;
    }
    .review-q-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .review-q-card {
      background: rgba(0,0,0,0.18);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      margin-bottom: 0.75rem;
    }
    .review-q-card.correct { border-left: 4px solid var(--green); }
    .review-q-card.wrong { border-left: 4px solid var(--red); }
    .review-header {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 0.75rem;
      font-size: 0.82rem;
      font-weight: 700;
    }
    .review-outcome-text.correct { color: var(--green); }
    .review-outcome-text.wrong { color: var(--red); }
    .review-q-txt {
      font-size: 0.9rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
    }
    .review-opts {
      list-style-type: none;
      padding-left: 1rem;
      font-size: 0.82rem;
      margin-bottom: 0.75rem;
    }
    .review-opt-li {
      margin-bottom: 0.35rem;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .review-opt-li.selected-correct {
      background: rgba(74, 222, 128, 0.15);
      border: 1px solid var(--green);
      color: var(--green);
    }
    .review-opt-li.selected-wrong {
      background: rgba(248, 113, 113, 0.15);
      border: 1px solid var(--red);
      color: var(--red);
    }
    .review-opt-li.missed {
      border: 1px dashed var(--green);
      color: var(--green);
    }
    .review-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
      background: rgba(255,255,255,0.02);
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.03);
    }

    /* ─── PANE 5: SANDBOXES ───────────────────────── */
    .tab-bar {
      display: flex;
      gap: 0.25rem;
      margin-bottom: 1.25rem;
      background: var(--surface);
      border-radius: var(--radius-sm);
      padding: 4px;
      overflow-x: auto;
    }
    .tab-btn {
      padding: 6px 14px;
      border-radius: 8px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      font-family: inherit;
      font-size: 0.8rem;
      font-weight: 600;
      transition: var(--transition);
      white-space: nowrap;
    }
    .tab-btn.active {
      background: var(--surface-hover);
      color: var(--accent2);
    }
    .tab-pane {
      display: none;
    }
    .tab-pane.active {
      display: block;
      animation: fadeIn 0.3s;
    }
    .sandbox-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }
    @media (max-width: 800px) {
      .sandbox-split {
        grid-template-columns: 1fr;
      }
    }
    .field-label {
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 600;
      margin-bottom: 4px;
    }
    .sandbox-input {
      width: 100%;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xs);
      padding: 8px 12px;
      color: var(--text);
      font-family: var(--mono);
      font-size: 0.82rem;
      outline: none;
      transition: var(--transition);
    }
    .sandbox-input:focus {
      border-color: var(--accent2);
    }
    .sandbox-btn {
      padding: 8px 16px;
      border-radius: var(--radius-xs);
      border: none;
      cursor: pointer;
      background: linear-gradient(135deg, var(--accent2), var(--accent2-dim));
      color: #000;
      font-weight: 700;
      transition: var(--transition);
    }
    .sandbox-btn:hover {
      box-shadow: 0 0 12px var(--accent2-glow);
    }
    .sandbox-btn.orange {
      background: linear-gradient(135deg, var(--accent), var(--accent-dim));
      color: #fff;
    }
    .sandbox-btn.orange:hover {
      box-shadow: 0 0 12px var(--accent-glow);
    }
    .result-box {
      background: rgba(0,0,0,0.3);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
      padding: 1rem;
      font-family: var(--mono);
      font-size: 0.78rem;
      line-height: 1.8;
      min-height: 80px;
    }
    .result-box .rl { color: var(--text-muted); }
    .result-box .rv { color: var(--accent2); font-weight: 600; }
    .result-box .ro { color: var(--accent); font-weight: 600; }
    .result-box .rg { color: var(--green); font-weight: 600; }
    .result-box .rr { color: var(--red); font-weight: 600; }

    /* CPU GANTT CHART */
    .gantt-wrap {
      margin-top: 1rem;
    }
    .gantt {
      display: flex;
      height: 38px;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid var(--border-light);
    }
    .g-seg {
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.68rem;
      font-weight: 700;
      font-family: var(--mono);
      padding: 2px 4px;
      text-align: center;
      border-right: 1px solid rgba(0,0,0,0.25);
      min-width: 28px;
      flex-shrink: 0;
    }
    .g-seg:last-child { border-right: none; }
    .g-labels {
      display: flex;
      font-size: 0.62rem;
      font-family: var(--mono);
      color: var(--text-muted);
      margin-top: 2px;
    }
    .g-lbl {
      text-align: left;
      min-width: 28px;
    }

    /* LINUX TERMINAL CHALLENGE */
    .terminal-box {
      background: #02040a;
      border: 1px solid #161b22;
      border-radius: var(--radius-sm);
      overflow: hidden;
    }
    .terminal-header {
      background: #161b22;
      padding: 6px 12px;
      font-size: 0.72rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .terminal-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }
    .terminal-body {
      padding: 1rem;
      font-family: var(--mono);
      font-size: 0.8rem;
      line-height: 1.5;
      min-height: 200px;
    }
    .term-input-row {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 0.5rem;
    }
    .term-prompt {
      color: var(--accent2);
    }
    .term-text-input {
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      font-family: var(--mono);
      font-size: 0.8rem;
      outline: none;
    }

    /* ─── PANE 6: CRAM MATERIAL ──────────────────── */
    .cram-sections-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }
    @media (max-width: 900px) {
      .cram-sections-grid {
        grid-template-columns: 1fr;
      }
    }
    /* MATCH GAME */
    .match-grid-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }
    .match-card-item {
      padding: 0.55rem 0.88rem;
      border-radius: var(--radius-xs);
      cursor: pointer;
      font-size: 0.78rem;
      font-weight: 500;
      line-height: 1.45;
      border: 1px solid transparent;
      background: var(--surface);
      transition: all 0.2s;
      user-select: none;
    }
    .match-card-item:hover {
      border-color: var(--border);
    }
    .match-card-item.selected {
      border-color: var(--accent2);
      background: rgba(34, 211, 238, 0.08);
      color: var(--accent2);
    }
    .match-card-item.matched {
      opacity: 0.35;
      pointer-events: none;
      border-color: rgba(34, 211, 238, 0.12);
    }
    .match-card-item.wrong {
      animation: shake 0.4s ease;
    }
    .match-card-item.glow {
      border-color: var(--accent2) !important;
      box-shadow: 0 0 15px rgba(34, 211, 238, 0.32);
    }
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20% { transform: translateX(-6px); }
      40% { transform: translateX(6px); }
      60% { transform: translateX(-4px); }
      80% { transform: translateX(4px); }
    }
    .match-stats-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      font-size: 0.78rem;
      color: var(--text-muted);
    }
    .match-bar-track {
      flex: 1;
      height: 4px;
      background: var(--surface);
      border-radius: 99px;
      overflow: hidden;
    }
    .match-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent2), var(--accent));
      width: 0%;
      transition: width 0.4s;
    }

    /* CHEAT TABLES */
    .cheat-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.78rem;
    }
    .cheat-table th {
      padding: 6px 10px;
      text-align: left;
      font-size: 0.65rem;
      font-weight: 600;
      color: var(--text-muted);
      letter-spacing: 0.06em;
      text-transform: uppercase;
      border-bottom: 1px solid var(--border);
    }
    .cheat-table td {
      padding: 6px 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.03);
      vertical-align: top;
      line-height: 1.45;
    }
    .cheat-table tr:last-child td { border-bottom: none; }
    .layer-index {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      border-radius: 4px;
      font-size: 0.65rem;
      font-weight: 700;
      font-family: var(--mono);
      background: var(--surface);
    }
    .li-cyan { color: var(--accent2); background: rgba(34, 211, 238, 0.15); }
    .li-orange { color: var(--accent); background: rgba(249, 115, 22, 0.15); }

    /* ANKI COPY BOX */
    .anki-copy-area {
      width: 100%;
      height: 180px;
      background: #020408;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-xs);
      padding: 8px 12px;
      color: var(--text-muted);
      font-family: var(--mono);
      font-size: 0.72rem;
      outline: none;
      resize: none;
    }
  </style>
</head>
<body>
  <div class="mesh-bg"></div>

  <!-- ─── HEADER ─── -->
  <header>
    <div class="header-inner">
      <a href="../index.html" class="logo-container">
        <span class="logo-badge">🚀</span>
        <div class="logo-text">OS·NET <span>Master</span></div>
        <span class="syllabus-code">ETE2AE</span>
      </a>
      
      <nav class="main-nav">
        <button class="nav-btn active" id="nav-checklist" onclick="switchView('checklist')">📋 Checklist</button>
        <button class="nav-btn" id="nav-flashcards" onclick="switchView('flashcards')">⚡ Flashcards</button>
        <button class="nav-btn" id="nav-memorize" onclick="switchView('memorize')">🧠 Memorize</button>
        <button class="nav-btn" id="nav-exam" onclick="switchView('exam')">📝 Mock Exam</button>
        <button class="nav-btn" id="nav-tools" onclick="switchView('tools')">🛠️ Sandboxes</button>
        <button class="nav-btn" id="nav-cram" onclick="switchView('cram')">📚 Cram Material</button>
      </nav>

      <div class="offline-badge">
        <span class="offline-dot"></span>
        Offline Cramming
      </div>
    </div>
  </header>

  <!-- ─── MAIN CONTENT ─── -->
  <main>
    
    <!-- ─── STATS HERO PANEL ─── -->
    <div class="hero-stats-panel">
      <!-- 2-Hour Study Timer -->
      <div class="glass-panel time-tracker-box" style="margin-bottom:0;">
        <div class="timer-circle">⏱️</div>
        <div class="timer-info">
          <h3 id="cram-countdown">02:00:00</h3>
          <p>Time Left for Exam Preparation</p>
        </div>
      </div>

      <!-- Checklist Mastery Progress -->
      <div class="glass-panel stats-card-box" style="margin-bottom:0;">
        <div class="stats-card-details">
          <h4>Mastered</h4>
          <p id="stat-mastered-q">0 / 64</p>
        </div>
        <div class="stats-donut-container">
          <svg width="60" height="60" viewBox="0 0 60 60">
            <circle cx="30" cy="30" r="25" fill="transparent" stroke="rgba(255,255,255,0.03)" stroke-width="6"></circle>
            <circle id="donut-mastered-stroke" cx="30" cy="30" r="25" fill="transparent" stroke="var(--accent2)" stroke-width="6" stroke-dasharray="157" stroke-dashoffset="157" transform="rotate(-90 30 30)" stroke-linecap="round"></circle>
          </svg>
          <div class="stats-donut-label" id="stat-mastery-pct">0%</div>
        </div>
      </div>

      <!-- Needs Review Progress -->
      <div class="glass-panel stats-card-box" style="margin-bottom:0;">
        <div class="stats-card-details">
          <h4>Needs Review</h4>
          <p id="stat-review-q">0 / 64</p>
        </div>
        <div class="stats-donut-container">
          <svg width="60" height="60" viewBox="0 0 60 60">
            <circle cx="30" cy="30" r="25" fill="transparent" stroke="rgba(255,255,255,0.03)" stroke-width="6"></circle>
            <circle id="donut-review-stroke" cx="30" cy="30" r="25" fill="transparent" stroke="var(--accent)" stroke-width="6" stroke-dasharray="157" stroke-dashoffset="157" transform="rotate(-90 30 30)" stroke-linecap="round"></circle>
          </svg>
          <div class="stats-donut-label" id="stat-review-pct">0%</div>
        </div>
      </div>
    </div>


    <!-- ─── PANE 1: CHECKLIST ─── -->
    <div class="view-pane active" id="pane-checklist">
      <div class="glass-panel glowing">
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
          <div>
            <h2 style="font-size: 1.45rem; font-weight: 800;">📋 Concept Checklist &amp; Active Recall</h2>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">
              Expand each card to study its content. Click the <span style="color:#f43f5e; font-weight:700;">pink-blurred words</span> to test yourself!
            </p>
          </div>
          <button class="fc-btn" id="checklist-reveal-btn" onclick="toggleRevealAll()" style="min-width: 170px;">👁️ Reveal Answers</button>
        </div>

        <div class="checklist-controls">
          <div class="search-bar-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" class="search-input" id="checklist-search" placeholder="Filter by keyword (e.g. swap, port, scheduling)..." oninput="handleSearch()">
          </div>
          <div class="filter-tags" id="checklist-category-filters">
            <button class="filter-btn active" onclick="filterCategory('All', this)">All</button>
            <button class="filter-btn" onclick="filterCategory('OS Basics & Architecture', this)">🖥️ OS Basics</button>
            <button class="filter-btn" onclick="filterCategory('Process Management', this)">🔄 Processes</button>
            <button class="filter-btn" onclick="filterCategory('Memory Management', this)">💾 Memory</button>
            <button class="filter-btn" onclick="filterCategory('File Systems & Sharing Models', this)">📁 File Systems</button>
            <button class="filter-btn" onclick="filterCategory('Computer Networks', this)">🌐 Networking</button>
            <button class="filter-btn" onclick="filterCategory('CLI & Diagnostics', this)">🐧 CLI</button>
            <button class="filter-btn" onclick="filterCategory('Step-by-Step Calculations', this)">🔢 Math</button>
          </div>
        </div>

        <div class="checklist-grid" id="checklist-questions-container">
          <!-- Populated by JavaScript -->
        </div>
      </div>
    </div>


    <!-- ─── PANE 2: FLASHCARDS ─── -->
    <div class="view-pane" id="pane-flashcards">
      <div class="glass-panel glowing">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <h2 style="font-size: 1.45rem; font-weight: 800;">⚡ Active-Recall Flashcards</h2>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Rate cards to update your study deck. Weak cards go to the "Weak" deck automatically.</p>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <select class="sandbox-input" id="fc-category-select" onchange="initFlashcards()" style="width: 220px; height: 36px; padding: 6px 10px;">
              <option value="All">All Decks</option>
              <option value="OS Basics & Architecture">🖥️ OS Basics</option>
              <option value="Process Management">🔄 Process Management</option>
              <option value="Memory Management">💾 Memory Management</option>
              <option value="File Systems & Sharing Models">📁 File Systems</option>
              <option value="Computer Networks">🌐 Computer Networks</option>
              <option value="CLI & Diagnostics">🐧 CLI &amp; Diagnostics</option>
              <option value="Step-by-Step Calculations">🔢 Calculations</option>
              <option value="Weak">⚠️ Weak Cards (Rated Red)</option>
            </select>
            <button class="fc-btn" onclick="shuffleFlashcards()" style="height:36px; padding:0 12px;">🔀 Shuffle</button>
          </div>
        </div>

        <div class="flashcard-stage">
          <div class="fc-progress-bar-wrap">
            <div class="fc-progress-bar-fill" id="fc-progress-bar-fill"></div>
          </div>
          
          <div class="fc-stats-panel">
            <div class="fc-stat-item">Known: <span id="fc-stat-known" style="color:var(--green)">0</span></div>
            <div class="fc-stat-item">Weak: <span id="fc-stat-weak" style="color:var(--accent)">0</span></div>
            <div class="fc-stat-item">Total: <span id="fc-stat-total">64</span></div>
          </div>

          <div class="fc-box-wrap" onclick="flipCard()">
            <div class="fc-card-body" id="fc-card-body">
              <div class="fc-card-face fc-card-front">
                <span class="fc-card-cat" id="fc-front-cat">OS Basics</span>
                <p class="fc-card-q" id="fc-front-q">What is the primary purpose of an Operating System, and what are the three key system resources it controls and allocates?</p>
                <span class="fc-card-tap-hint">Click or press Space to reveal answer</span>
              </div>
              <div class="fc-card-face fc-card-back">
                <span class="fc-card-cat" id="fc-back-cat" style="color:var(--accent);">OS Basics</span>
                <div class="fc-card-ans" id="fc-back-a">Answer content...</div>
                <span class="fc-card-tap-hint" style="color:var(--text-muted)">Click again to flip back</span>
              </div>
            </div>
          </div>

          <div class="fc-controls-row">
            <button class="fc-btn bad" onclick="rateCard('weak', event)">✗ Still Learning (1)</button>
            <button class="fc-btn" onclick="prevCard(event)">◀ Prev (Left)</button>
            <button class="fc-btn primary" onclick="flipCard(); event.stopPropagation();">↺ Flip (Space)</button>
            <button class="fc-btn" onclick="nextCard(event)">Next (Right) ▶</button>
            <button class="fc-btn good" onclick="rateCard('known', event)">✓ Know It! (2)</button>
          </div>
          
          <div class="fc-shortcuts">
            <span><kbd>Space</kbd> Flip</span>
            <span><kbd>←</kbd> <kbd>→</kbd> Navigate</span>
            <span><kbd>1</kbd> Mark Weak</span>
            <span><kbd>2</kbd> Mark Known</span>
            <span><kbd>R</kbd> Shuffle</span>
          </div>
        </div>
      </div>
    </div>


    <!-- ─── PANE 3: MEMORIZE ─── -->
    <div class="view-pane" id="pane-memorize">
      <div class="glass-panel glowing">
        <h2 style="font-size: 1.45rem; font-weight: 800; margin-bottom: 0.25rem;">🧠 Audio Narrator &amp; Podcasts</h2>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.25rem;">
          Re-listen to the entire 64 card syllabus. Reliable natural voice downloads solve phone lockscreen interruptions.
        </p>

        <!-- Natural Voice Podcast Selector -->
        <div class="glass-panel" style="margin-bottom: 1.5rem; padding: 1.25rem; background: rgba(34, 211, 238, 0.05); border: 1px solid rgba(34, 211, 238, 0.2);">
          <div style="display: flex; align-items: center; gap: 1.25rem; flex-wrap: wrap;">
            <div style="font-size: 2.2rem; flex-shrink: 0;">🎙️</div>
            <div style="flex: 1; min-width: 260px;">
              <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text); margin-bottom: 0.25rem;">Pre-recorded Audio Podcast Guide (Lock-Screen Safe)</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.75rem;">If your browser's TTS cuts out in background tabs or on lock-screen, select and download an MP3 track below:</p>
              
              <div style="margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
                <label for="oscn-audio-voice" style="font-size: 0.78rem; color: var(--text-muted); font-weight: 700;">Accent/Voice: </label>
                <select id="oscn-audio-voice" onchange="changeOSCNAudioVoice()" style="background: var(--surface); border: 1px solid var(--border); color: #fff; padding: 6px 12px; border-radius: 6px; font-size: 0.82rem; outline: none; cursor: pointer;">
                  <option value="oscn_audio_guide_us_male.mp3" selected>🇺🇸 US Male (Steffan)</option>
                  <option value="oscn_audio_guide_us_female.mp3">🇺🇸 US Female (Jenny)</option>
                  <option value="oscn_audio_guide_uk_male.mp3">🇬🇧 UK Male (Ryan)</option>
                  <option value="oscn_audio_guide_uk_female.mp3">🇬🇧 UK Female (Sonia)</option>
                </select>
              </div>

              <audio id="oscn-audio-player" controls preload="none" style="width: 100%; max-width: 380px; outline: none;">
                <source id="oscn-audio-source" src="oscn_audio_guide_us_male.mp3" type="audio/mpeg">
                Your browser does not support the audio element.
              </audio>
            </div>
            <a id="oscn-audio-download" href="oscn_audio_guide_us_male.mp3" download class="fc-btn primary" style="text-decoration: none; font-weight: 700; min-width: 140px; text-align: center; height: 38px; display: inline-flex; align-items: center; justify-content: center;">⬇️ Download MP3</a>
          </div>
        </div>

        <!-- Browser TTS Narrator Playlist -->
        <div class="glass-panel" style="padding: 1.25rem; background: rgba(0,0,0,0.2);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; border-bottom:1px solid var(--border); padding-bottom:0.75rem; margin-bottom:1rem;">
            <h3 style="font-size:1.05rem; font-weight:700; color:var(--accent2)">🔊 Browser TTS Reader (Play All 20 Tracks)</h3>
            <div style="display:flex; gap:0.5rem; align-items:center; flex-wrap:wrap;">
              <span id="tts-playlist-status" style="font-size:0.78rem; color:var(--text-muted)">Stopped. Click Play All to listen.</span>
              <span id="tts-playlist-counter" style="font-size:0.8rem; font-weight:700; color:var(--accent2); font-family:var(--mono);">0 / 20</span>
            </div>
          </div>

          <div class="checklist-controls" style="margin-bottom:1rem;">
            <button class="fc-btn primary" id="tts-play-btn" onclick="playTTSPlaylist()">▶ Play All</button>
            <button class="fc-btn" id="tts-pause-btn" onclick="pauseTTSPlaylist()" disabled>⏸ Pause</button>
            <button class="fc-btn" onclick="stopTTSPlaylist()">⏹ Stop</button>
            
            <div style="display:flex; align-items:center; gap:0.5rem; font-size:0.8rem;">
              <span style="color:var(--text-muted)">Speed:</span>
              <select id="tts-speed-select" onchange="updateTTSSpeed()" style="background:var(--surface); border:1px solid var(--border); color:#fff; padding:4px 8px; border-radius:6px;">
                <option value="0.7">0.7x</option>
                <option value="0.85" selected>0.85x (Study)</option>
                <option value="1.0">1.0x</option>
                <option value="1.2">1.2x</option>
                <option value="1.5">1.5x</option>
              </select>
            </div>

            <div style="display:flex; align-items:center; gap:0.5rem; font-size:0.8rem;">
              <span style="color:var(--text-muted)">Voice:</span>
              <select id="tts-voice-select" style="background:var(--surface); border:1px solid var(--border); color:#fff; padding:4px 8px; border-radius:6px; max-width:200px;">
                <option value="">Default English</option>
              </select>
            </div>
          </div>

          <div class="result-box" id="tts-now-playing-panel" style="min-height:50px; margin-bottom:1rem; border-left:3px solid var(--accent2);">
            <span style="color:var(--text-muted)">Playlist not active. Press Play All to start reading the checklist.</span>
          </div>

          <div class="g-labels" style="font-weight:700; font-size:0.68rem; letter-spacing:0.05em; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.25rem;">Auto-Read Playlist Tracks</div>
          <div class="cmd-list" id="tts-playlist-items-container" style="max-height:220px;">
            <!-- Dynamically populated playlist tracks -->
          </div>
        </div>

      </div>
    </div>


    <!-- ─── PANE 4: MOCK EXAM ─── -->
    <div class="view-pane" id="pane-exam">
      <!-- Start Exam State -->
      <div class="glass-panel glowing" id="exam-start-state">
        <div class="exam-start-panel">
          <div class="exam-icon">📝</div>
          <h2 style="font-size:1.8rem; font-weight:800; margin-bottom:0.75rem;">Timed Mock Exam Simulator</h2>
          <p style="color:var(--text-muted); font-size:0.92rem; margin-bottom:2rem;">
            Test your knowledge under pressure. The simulator will compile a random **30-question** exam from the 64 course cards. You must answer them within a **30-minute** limit. Passing score is **60% (18/30)**.
          </p>
          
          <div style="display:flex; justify-content:center; gap:0.5rem; margin-bottom:2.25rem;">
            <select class="sandbox-input" id="exam-topic-select" style="max-width:320px;">
              <option value="All">All Topics (Balanced Mix)</option>
              <option value="OS Basics & Architecture">OS Basics &amp; Hypervisors</option>
              <option value="Process Management">Process Scheduling &amp; Deadlocks</option>
              <option value="Memory Management">Virtual Memory &amp; Page Replacement</option>
              <option value="File Systems & Sharing Models">File Systems &amp; Models</option>
              <option value="Computer Networks">Networking &amp; VLANs</option>
              <option value="CLI & Diagnostics">Linux Commands &amp; Diagnostics</option>
              <option value="Step-by-Step Calculations">Math Calculations Walkthrough</option>
            </select>
          </div>

          <button class="exam-btn" onclick="startExam()">🚀 Start Exam Simulator</button>
        </div>
      </div>

      <!-- Active Exam State -->
      <div class="glass-panel glowing" id="exam-run-state" style="display:none;">
        <div class="exam-run-header">
          <div>
            <h2 style="font-size:1.35rem; font-weight:800;" id="exam-heading">Active Mock Exam</h2>
            <p style="color:var(--text-muted); font-size:0.8rem; margin-top:2px;" id="exam-subheading">Question 1 of 30</p>
          </div>
          <div class="exam-timer" id="exam-timer">
            ⏱️ <span id="exam-timer-val">30:00</span>
          </div>
        </div>

        <!-- Tracker dots -->
        <div class="exam-tracker" id="exam-tracker">
          <!-- 30 dots dynamically generated -->
        </div>

        <!-- Question Box -->
        <div class="exam-q-box" id="exam-q-box">
          <!-- Active Question content here -->
        </div>

        <!-- Nav row -->
        <div class="exam-nav-row">
          <button class="fc-btn" onclick="examPrev()" id="exam-prev-btn">◀ Previous</button>
          <button class="exam-btn" onclick="confirmSubmitExam()" style="padding:10px 24px; font-size:0.9rem; background:linear-gradient(135deg, var(--green), #059669); box-shadow: 0 0 15px rgba(74,222,128,0.25);">✓ Submit Exam</button>
          <button class="fc-btn" onclick="examNext()" id="exam-next-btn">Next ▶</button>
        </div>
      </div>

      <!-- Exam Results State -->
      <div class="glass-panel glowing" id="exam-results-state" style="display:none;">
        <h2 style="font-size:1.8rem; font-weight:800; margin-bottom:1.5rem;">Mock Exam Diagnostic Report</h2>
        
        <div class="sandbox-split" style="margin-bottom: 2rem;">
          <!-- Donut Score -->
          <div class="results-donut-box">
            <div class="results-score-circle">
              <svg width="140" height="140" viewBox="0 0 140 140">
                <circle cx="70" cy="70" r="58" fill="transparent" stroke="rgba(255,255,255,0.04)" stroke-width="12"></circle>
                <circle id="results-stroke-fill" cx="70" cy="70" r="58" fill="transparent" stroke="var(--accent2)" stroke-width="12" stroke-dasharray="364.4" stroke-dashoffset="364.4" stroke-linecap="round" transform="rotate(-90 70 70)"></circle>
              </svg>
              <div class="score-circle-text">
                <span id="results-score-text">0/30</span>
                <span class="score-circle-label" id="results-pct-text">0%</span>
              </div>
            </div>
            <div class="results-outcome pass" id="results-outcome">PASSED</div>
          </div>
          
          <!-- Category Diagnostics -->
          <div class="results-diag-box">
            <div class="diag-title">Category Strength Diagnostic</div>
            <div class="diag-bars" id="results-category-bars">
              <!-- Dynamically populated bars -->
            </div>
          </div>
        </div>

        <div style="display:flex; justify-content:center; gap:1rem; margin-bottom:2.5rem;">
          <button class="exam-btn" onclick="restartExam()" style="background:var(--surface); border:1px solid var(--border); box-shadow:none; color:var(--text);">↺ Try Another Exam</button>
          <button class="exam-btn" onclick="switchView('checklist')">📋 Go to Checklist to Study</button>
        </div>

        <div class="results-review-title">Detailed Answers Review</div>
        <div class="review-q-list" id="results-review-list">
          <!-- List of exam questions with answers, correctness marked -->
        </div>
      </div>
    </div>


    <!-- ─── PANE 5: SANDBOXES ─── -->
    <div class="view-pane" id="pane-tools">
      <div class="glass-panel glowing">
        <div class="tab-bar">
          <button class="tab-btn active" onclick="switchSandboxTab('sand-cpu', this)">🖥️ CPU Scheduling</button>
          <button class="tab-btn" onclick="switchSandboxTab('sand-subnet', this)">🌐 Subnetting Calc</button>
          <button class="tab-btn" onclick="switchSandboxTab('sand-page', this)">💾 Page Replacement</button>
          <button class="tab-btn" onclick="switchSandboxTab('sand-ip', this)">🔢 IP Converter</button>
          <button class="tab-btn" onclick="switchSandboxTab('sand-terminal', this)">🐧 Linux CLI Challenge</button>
        </div>

        <!-- SUBTAB 1: CPU SCHEDULING SIMULATOR -->
        <div class="tab-pane active" id="sand-cpu">
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
            Run scheduling algorithms (First-Come, First-Served; Shortest Job First; and Round Robin) to generate Gantt charts and average waiting times.
          </p>
          <div class="sandbox-split">
            <div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">Processes (Format: Name, Arrival, Burst — one per line)</label>
                <textarea class="sandbox-input" id="cpu-procs" rows="5" style="resize:vertical">P1, 0, 6&#10;P2, 1, 4&#10;P3, 2, 2</textarea>
              </div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">Algorithm</label>
                <select class="sandbox-input" id="cpu-algo" style="cursor:pointer;">
                  <option value="fcfs">FCFS (First-Come, First-Served)</option>
                  <option value="sjf">SJF (Shortest Job First - Non-preemptive)</option>
                  <option value="rr">Round Robin</option>
                </select>
              </div>
              <div class="fl" style="margin-bottom: 1rem;">
                <label class="field-label">Time Quantum (Round Robin only)</label>
                <input class="sandbox-input" id="cpu-quantum" type="number" value="2" min="1">
              </div>
              <button class="sandbox-btn" onclick="runCPU()">▶ Calculate &amp; Build Gantt</button>
            </div>
            <div>
              <div class="diag-title">Results &amp; Gantt Chart</div>
              <div class="result-box" id="cpu-result" style="margin-bottom: 1rem;">Enter process configuration and click Calculate.</div>
              <div class="gantt-wrap" id="gantt-wrap" style="display:none;">
                <div class="gantt" id="gantt"></div>
                <div class="g-labels" id="g-labels"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- SUBTAB 2: SUBNETTING CALCULATOR -->
        <div class="tab-pane" id="sand-subnet">
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
            Compute network parameters, broadcast address, host range, and host count from an IP and CIDR mask.
          </p>
          <div class="sandbox-split">
            <div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">IP Address</label>
                <input type="text" class="sandbox-input" id="sub-ip" value="192.168.10.138">
              </div>
              <div class="fl" style="margin-bottom: 1.25rem;">
                <label class="field-label">Prefix Length (CIDR mask)</label>
                <input type="number" class="sandbox-input" id="sub-prefix" value="26" min="1" max="32">
              </div>
              <button class="sandbox-btn" onclick="runSubnet()">▶ Calculate Subnet</button>
            </div>
            <div>
              <div class="diag-title">Network Parameters</div>
              <div class="result-box" id="subnet-result">Enter IP address details and click Calculate.</div>
            </div>
          </div>
        </div>

        <!-- SUBTAB 3: PAGE REPLACEMENT SIMULATOR -->
        <div class="tab-pane" id="sand-page">
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
            Simulate virtual memory page frame allocation and count page faults step-by-step.
          </p>
          <div class="sandbox-split">
            <div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">Reference String (space-separated integers)</label>
                <input type="text" class="sandbox-input" id="page-ref" value="7 0 1 2 0 3">
              </div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">Available Memory Frames</label>
                <input type="number" class="sandbox-input" id="page-frames" value="3" min="1" max="8">
              </div>
              <div class="fl" style="margin-bottom: 1.25rem;">
                <label class="field-label">Replacement Algorithm</label>
                <select class="sandbox-input" id="page-algo" style="cursor:pointer;">
                  <option value="fifo">FIFO (First-In, First-Out)</option>
                  <option value="lru">LRU (Least Recently Used)</option>
                </select>
              </div>
              <button class="sandbox-btn orange" onclick="runPage()">▶ Run Page Simulation</button>
            </div>
            <div>
              <div class="diag-title">Fault Report</div>
              <div class="result-box" id="page-result" style="margin-bottom: 1rem;">Click Run to calculate faults.</div>
              <div id="page-table-wrap" style="overflow-x:auto; display:none;"></div>
            </div>
          </div>
        </div>

        <!-- SUBTAB 4: IP BINARY CONVERTER -->
        <div class="tab-pane" id="sand-ip">
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
            Quickly translate decimal IP addresses to binary, or binary IP strings back to decimal format.
          </p>
          <div class="sandbox-split">
            <div>
              <div class="diag-title">Decimal to Binary</div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">Decimal IP (x.x.x.x)</label>
                <input type="text" class="sandbox-input" id="d2b-input" value="172.16.254.1">
              </div>
              <button class="sandbox-btn" onclick="decToBin()" style="margin-bottom:1rem;">▶ Convert to Binary</button>
              <div class="result-box" id="d2b-result">Output will show binary representation...</div>
            </div>
            <div>
              <div class="diag-title">Binary to Decimal</div>
              <div class="fl" style="margin-bottom: 0.75rem;">
                <label class="field-label">Binary IP (8 bits per octet, dot-separated)</label>
                <input type="text" class="sandbox-input" id="b2d-input" value="10101100.00010000.11111110.00000001">
              </div>
              <button class="sandbox-btn orange" onclick="binToDec()" style="margin-bottom:1rem;">▶ Convert to Decimal</button>
              <div class="result-box" id="b2d-result">Output will show decimal IP representation...</div>
            </div>
          </div>
        </div>

        <!-- SUBTAB 5: LINUX TERMINAL CHALLENGE -->
        <div class="tab-pane" id="sand-terminal">
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
            Test your knowledge of standard Linux commands. Type the correct command syntax to solve the current challenge.
          </p>
          <div class="sandbox-split">
            <div>
              <div style="background:rgba(255,255,255,0.02); border:1px solid var(--border); border-radius: var(--radius-sm); padding:1rem; min-height: 250px; display:flex; flex-direction:column; justify-content:space-between;">
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:0.75rem;">
                    <span style="font-weight:700; color:var(--accent2); font-size:0.85rem;">Terminal Challenge</span>
                    <span style="font-family:var(--mono); font-size:0.75rem; color:var(--text-muted);" id="term-challenge-progress">Task 1 of 5</span>
                  </div>
                  <h4 style="font-size:0.95rem; font-weight:800; margin-bottom:0.5rem;" id="term-challenge-title">Active Challenge</h4>
                  <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.5;" id="term-challenge-desc">Description of task...</p>
                  <div style="margin-top:0.75rem; font-size:0.75rem; color:var(--yellow); display:none;" id="term-challenge-hint-box"><strong>💡 Hint:</strong> <span id="term-challenge-hint-txt">hint</span></div>
                </div>
                <div style="display:flex; gap:0.5rem; margin-top:1rem;">
                  <button class="fc-btn" onclick="showTerminalChallengeHint()" style="padding:6px 12px; font-size:0.72rem;">💡 Show Hint</button>
                  <button class="fc-btn" onclick="skipTerminalChallenge()" style="padding:6px 12px; font-size:0.72rem;">⏭ Skip</button>
                  <button class="fc-btn primary" onclick="resetTerminalChallenge()" style="padding:6px 12px; font-size:0.72rem; margin-left:auto;">🔄 Restart Game</button>
                </div>
              </div>
            </div>
            
            <div class="terminal-box">
              <div class="terminal-header">
                <div class="terminal-dot" style="background:#ff5f56;"></div>
                <div class="terminal-dot" style="background:#ffbd2e;"></div>
                <div class="terminal-dot" style="background:#27c93f;"></div>
                <span style="margin-left: 0.5rem; font-family:var(--mono);">bash -- interactive terminal</span>
              </div>
              <div class="terminal-body">
                <div style="color:var(--text-muted); margin-bottom: 0.75rem;" id="term-console-history">
                  Welcome to GNU bash, version 5.1.16-release (x86_64-pc-linux-gnu)<br>
                  Type the correct command below and press Enter to evaluate.<br><br>
                </div>
                <div class="term-input-row">
                  <span class="term-prompt">vokoun@ete2ae:~$</span>
                  <input type="text" class="term-text-input" id="term-user-input" placeholder="type command here..." autofocus onkeydown="handleTerminalKeyPress(event)">
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>


    <!-- ─── PANE 6: CRAM MATERIAL ─── -->
    <div class="view-pane" id="pane-cram">
      <div class="cram-sections-grid">
        
        <!-- COLUMN 1 -->
        <div>
          <!-- Definitions Matcher -->
          <div class="glass-panel glowing">
            <h2 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 0.25rem;">🎯 Definitions Matcher</h2>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 1rem;">Link the correct OS &amp; Network terms. Get all 8 correct to master the set.</p>
            
            <div class="match-stats-row">
              <span id="mscore-text">0 / 8 Matched</span>
              <div class="match-bar-track">
                <div class="match-bar-fill" id="mscore-bar"></div>
              </div>
              <span id="mscore-pct" style="font-weight:700; color:var(--accent2)">0%</span>
              <button class="filter-btn" onclick="resetMatcher()" style="padding: 2px 8px; font-size: 0.7rem;">🔄 Reset</button>
            </div>
            
            <div class="match-grid-row" id="match-grid">
              <!-- Grid items injected by JS -->
            </div>
          </div>

          <!-- OSI 7-Layer Model Table -->
          <div class="glass-panel">
            <h2 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 0.75rem;">📶 OSI 7-Layer Model Cheat Sheet</h2>
            <table class="cheat-table">
              <thead>
                <tr>
                  <th>Layer</th>
                  <th>PDU</th>
                  <th>Protocols &amp; Key Devices</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><span class="layer-index li-orange">7</span> <b>Application</b></td>
                  <td>Data</td>
                  <td>HTTP, HTTPS, SSH, FTP, DNS, DHCP, SMTP</td>
                </tr>
                <tr>
                  <td><span class="layer-index li-orange">6</span> <b>Presentation</b></td>
                  <td>Data</td>
                  <td>TLS, SSL, ASCII, UTF-8, JPEG, compression</td>
                </tr>
                <tr>
                  <td><span class="layer-index li-orange">5</span> <b>Session</b></td>
                  <td>Data</td>
                  <td>NetBIOS, RPC, SQL connection management</td>
                </tr>
                <tr>
                  <td><span class="layer-index li-cyan">4</span> <b>Transport</b></td>
                  <td>Segment</td>
                  <td>TCP ( SYN → SYN-ACK → ACK ), UDP (connectionless)</td>
                </tr>
                <tr>
                  <td><span class="layer-index li-cyan">3</span> <b>Network</b></td>
                  <td>Packet</td>
                  <td>IP, ICMP (ping/tracert), ARP. <b>Device: Router</b></td>
                </tr>
                <tr>
                  <td><span class="layer-index li-cyan">2</span> <b>Data Link</b></td>
                  <td>Frame</td>
                  <td>Ethernet, MAC addresses, PPP. <b>Device: Switch</b></td>
                </tr>
                <tr>
                  <td><span class="layer-index">1</span> <b>Physical</b></td>
                  <td>Bits</td>
                  <td>Cables (Fiber/UTP), signals. <b>Devices: Hub, Repeater</b></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- COLUMN 2 -->
        <div>
          <!-- Key Ports Cheat Sheet -->
          <div class="glass-panel">
            <h2 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 0.75rem;">📡 Common Network Ports</h2>
            <table class="cheat-table">
              <thead>
                <tr>
                  <th>Service</th>
                  <th>Port</th>
                  <th>Transport</th>
                  <th>Syllabus Key Fact</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><span class="q-badge" style="color:var(--accent2);">HTTP</span></td>
                  <td><b>80</b></td>
                  <td>TCP</td>
                  <td>Web browsing, unencrypted plaintext transfer</td>
                </tr>
                <tr>
                  <td><span class="q-badge" style="color:var(--accent2);">HTTPS</span></td>
                  <td><b>443</b></td>
                  <td>TCP</td>
                  <td>Web browsing, encrypted via TLS/SSL</td>
                </tr>
                <tr>
                  <td><span class="q-badge" style="color:var(--accent);">SSH</span></td>
                  <td><b>22</b></td>
                  <td>TCP</td>
                  <td>Secure Shell remote access (encrypted channel)</td>
                </tr>
                <tr>
                  <td><span class="q-badge" style="color:var(--accent);">FTP</span></td>
                  <td><b>21</b></td>
                  <td>TCP</td>
                  <td>File Transfer Protocol (control port, plaintext)</td>
                </tr>
                <tr>
                  <td><span class="q-badge" style="color:var(--violet);">DNS</span></td>
                  <td><b>53</b></td>
                  <td>UDP / TCP</td>
                  <td>Distributed Database, resolves domain name (read right-to-left)</td>
                </tr>
                <tr>
                  <td><span class="q-badge" style="color:var(--violet);">DHCP</span></td>
                  <td><b>67 / 68</b></td>
                  <td>UDP</td>
                  <td>DORA broadcast assigns IP, mask, default gateway, DNS</td>
                </tr>
                <tr>
                  <td><span class="q-badge" style="color:var(--green);">SMTP</span></td>
                  <td><b>25</b></td>
                  <td>TCP</td>
                  <td>Simple Mail Transfer Protocol (outgoing mail routing)</td>
                </tr>
                <tr>
                  <td><span class="q-badge">ICMP</span></td>
                  <td><b>None</b></td>
                  <td>—</td>
                  <td>ping (echo request) &amp; traceroute (TTL expiry) — <b>no port numbers!</b></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Anki Deck Import TSV Copy Box -->
          <div class="glass-panel">
            <h2 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 0.25rem;">📇 OSCN Anki Deck Exporter</h2>
            <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 0.88rem;">
              Click in the text area below, copy the entire block, and paste it into a file named <code>anki_import.txt</code> to import it directly into Anki.
            </p>
            <textarea class="anki-copy-area" readonly onclick="this.select()" id="anki-tsv-copy-box"></textarea>
          </div>

          <!-- Hot Exam Traps & Warnings -->
          <div class="glass-panel" style="border-color: rgba(248,113,113,0.25); background: rgba(248,113,113,0.02);">
            <h2 style="font-size: 1.25rem; font-weight: 800; color: var(--red); margin-bottom: 0.5rem;">🔥 High-Yield Exam Warnings</h2>
            <ul style="list-style-type:none; font-size:0.8rem; line-height:1.6;">
              <li style="margin-bottom:0.5rem; position:relative; padding-left:1.25rem;">
                <span style="position:absolute; left:0; color:var(--red);">⚠️</span>
                <strong>Disk Defragmentation:</strong> Defragmentation is a <em>user utility tool</em>, NOT a core function of the OS kernel. This is a recurring exam trap!
              </li>
              <li style="margin-bottom:0.5rem; position:relative; padding-left:1.25rem;">
                <span style="position:absolute; left:0; color:var(--red);">⚠️</span>
                <strong>BIOS Storage Location:</strong> Stored in non-volatile <em>EEPROM or NAND flash</em> on the motherboard, NOT in physical RAM.
              </li>
              <li style="margin-bottom:0.5rem; position:relative; padding-left:1.25rem;">
                <span style="position:absolute; left:0; color:var(--red);">⚠️</span>
                <strong>Linux History:</strong> Linux is an open-source OS kernel written completely from scratch by Torvalds in 1991. It is <em>not</em> derived from Unix code.
              </li>
              <li style="margin-bottom:0.5rem; position:relative; padding-left:1.25rem;">
                <span style="position:absolute; left:0; color:var(--red);">⚠️</span>
                <strong>FAT16 Partition Size:</strong> Limited mathematically to <em>4 GB</em> by its 16-bit cluster addressing ($65,536 \\text{ clusters} \\times 64 \\text{ KB}$ max cluster size).
              </li>
            </ul>
          </div>
        </div>

      </div>
    </div>

  </main>

  <script>
    // ════════════════════════════════════════════════════════════════
    // DATABASE INJECTED
    // ════════════════════════════════════════════════════════════════
    const DATABASE = {database_json};

    const ANKI_DECK_TSV = `{anki_tsv}`;
    document.getElementById('anki-tsv-copy-box').value = ANKI_DECK_TSV;

    // Category mappings
    const CAT_LABELS = {{
      'OS Basics & Architecture': 'OS Basics',
      'Process Management': 'Processes',
      'Memory Management': 'Memory',
      'File Systems & Sharing Models': 'File Systems',
      'Computer Networks': 'Networking',
      'CLI & Diagnostics': 'CLI',
      'Step-by-Step Calculations': 'Calculations'
    }};

    // ════════════════════════════════════════════════════════════════
    // TIMERS & COUNTDOWN
    // ════════════════════════════════════════════════════════════════
    let countdownSecs = 7200;
    function updateCountdown() {{
      if (countdownSecs > 0) countdownSecs--;
      const h = Math.floor(countdownSecs / 3600);
      const m = Math.floor((countdownSecs % 3600) / 60);
      const s = countdownSecs % 60;
      const el = document.getElementById('cram-countdown');
      el.textContent = `${{String(h).padStart(2,'0')}}:${{String(m).padStart(2,'0')}}:${{String(s).padStart(2,'0')}}`;
      if (countdownSecs < 600) el.style.color = 'var(--red)';
      else if (countdownSecs < 1800) el.style.color = 'var(--yellow)';
    }}
    setInterval(updateCountdown, 1000);

    // ════════════════════════════════════════════════════════════════
    // NAVIGATION VIEWS
    // ════════════════════════════════════════════════════════════════
    function switchView(viewName) {{
      document.querySelectorAll('.view-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      
      const pane = document.getElementById('pane-' + viewName);
      const btn = document.getElementById('nav-' + viewName);
      if (pane) pane.classList.add('active');
      if (btn) btn.classList.add('active');
      
      // Stop TTS if switching away from memorize
      if (viewName !== 'memorize' && ttsPlaying) {{
        stopTTSPlaylist();
      }}
      
      window.scrollTo(0, 0);
    }}

    // ════════════════════════════════════════════════════════════════
    // ACTIVE RECALL REVEALS
    // ════════════════════════════════════════════════════════════════
    let revealState = false;
    function toggleRevealAll() {{
      revealState = !revealState;
      document.querySelectorAll('.blur-reveal').forEach(el => {{
        if (revealState) el.classList.add('revealed');
        else el.classList.remove('revealed');
      }});
      
      const btn = document.getElementById('checklist-reveal-btn');
      if (btn) btn.textContent = revealState ? '🙈 Hide All Answers' : '👁️ Reveal All Answers';
      
      const headerBtn = document.getElementById('reveal-all-btn');
      if (headerBtn) headerBtn.textContent = revealState ? '🙈 Hide Answers' : '👁️ Reveal Answers';
    }}

    // ════════════════════════════════════════════════════════════════
    // HELPER: HTML ESCAPE & HASH
    // ════════════════════════════════════════════════════════════════
    function htmlEscape(str) {{
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}
    function getQHash(str) {{
      let hash = 0;
      for (let i = 0; i < str.length; i++) {{
        hash = (hash << 5) - hash + str.charCodeAt(i);
        hash |= 0;
      }}
      return Math.abs(hash).toString();
    }}

    // ════════════════════════════════════════════════════════════════
    // CHECKLIST & STATS LOGIC
    // ════════════════════════════════════════════════════════════════
    let masteredIds = JSON.parse(localStorage.getItem('oscn_mastered') || '[]');
    let reviewIds = JSON.parse(localStorage.getItem('oscn_review') || '[]');
    let checklistCategory = 'All';

    function saveChecklistProgress() {{
      localStorage.setItem('oscn_mastered', JSON.stringify(masteredIds));
      localStorage.setItem('oscn_review', JSON.stringify(reviewIds));
      updateOverallStats();
    }}

    function updateOverallStats() {{
      const total = DATABASE.length;
      let masteredCount = 0;
      let reviewCount = 0;
      
      const hashes = DATABASE.map(q => getQHash(q.q));
      masteredIds.forEach(h => {{ if (hashes.includes(h)) masteredCount++; }});
      reviewIds.forEach(h => {{ if (hashes.includes(h)) reviewCount++; }});
      
      document.getElementById('stat-mastered-q').textContent = `${{masteredCount}} / ${{total}}`;
      document.getElementById('stat-review-q').textContent = `${{reviewCount}} / ${{total}}`;
      
      const masteredPct = Math.round((masteredCount / total) * 100) || 0;
      const reviewPct = Math.round((reviewCount / total) * 100) || 0;
      
      document.getElementById('stat-mastery-pct').textContent = `${{masteredPct}}%`;
      document.getElementById('stat-review-pct').textContent = `${{reviewPct}}%`;
      
      drawDonut('donut-mastered-stroke', masteredPct);
      drawDonut('donut-review-stroke', reviewPct);
    }}

    function drawDonut(strokeId, pct) {{
      const circle = document.getElementById(strokeId);
      if (!circle) return;
      // perimeter of r=25 is 157
      const offset = 157 - (pct / 100) * 157;
      circle.style.strokeDashoffset = offset;
    }}

    function toggleMasteryState(hash, state) {{
      if (state === 'mastered') {{
        const mIdx = masteredIds.indexOf(hash);
        if (mIdx > -1) {{
          masteredIds.splice(mIdx, 1);
        }} else {{
          masteredIds.push(hash);
          const rIdx = reviewIds.indexOf(hash);
          if (rIdx > -1) reviewIds.splice(rIdx, 1);
        }}
      }} else if (state === 'review') {{
        const rIdx = reviewIds.indexOf(hash);
        if (rIdx > -1) {{
          reviewIds.splice(rIdx, 1);
        }} else {{
          reviewIds.push(hash);
          const mIdx = masteredIds.indexOf(hash);
          if (mIdx > -1) masteredIds.splice(mIdx, 1);
        }}
      }}
      saveChecklistProgress();
      
      const itemEl = document.getElementById('card-' + hash);
      if (itemEl) {{
        itemEl.classList.remove('mastered', 'needs-review');
        const checkBtn = itemEl.querySelector('.m-btn.check');
        const starBtn = itemEl.querySelector('.m-btn.star');
        checkBtn.classList.remove('active');
        starBtn.classList.remove('active');
        
        if (masteredIds.includes(hash)) {{
          itemEl.classList.add('mastered');
          checkBtn.classList.add('active');
        }} else if (reviewIds.includes(hash)) {{
          itemEl.classList.add('needs-review');
          starBtn.classList.add('active');
        }}
      }}
    }}

    function toggleExpandRow(el) {{
      el.classList.toggle('expanded');
    }}

    function renderChecklist() {{
      const container = document.getElementById('checklist-questions-container');
      container.innerHTML = '';
      const query = document.getElementById('checklist-search').value.toLowerCase();
      
      DATABASE.forEach((q, idx) => {{
        if (checklistCategory !== 'All' && q.cat !== checklistCategory) return;
        
        const matchesQuery = q.q.toLowerCase().includes(query) || q.desc.toLowerCase().includes(query);
        if (!matchesQuery) return;
        
        const hash = getQHash(q.q);
        const isMastered = masteredIds.includes(hash);
        const isReview = reviewIds.includes(hash);
        
        let stateClass = '';
        if (isMastered) stateClass = 'mastered';
        else if (isReview) stateClass = 'needs-review';
        
        const card = document.createElement('div');
        card.className = `q-item-card ${{stateClass}}`;
        card.id = 'card-' + hash;
        
        // Wrap answer text with pink blurs for active recall
        // E.g. wrap bold text or core terms
        let parsedAns = q.desc;
        const blurWords = [
          "CPU time", "operating memory (RAM)", "local storage space (HDD/SSD)", "Kernel", "File System",
          "User Interface (UI)", "API", "Cooperative Multitasking", "Preemptive Multitasking", "battery-operated devices",
          "touchscreen as the primary interface", "Type 1 (Bare-Metal)", "Type 2 (Hosted)", "Copyleft", "Permissive",
          "EEPROM or NAND flash memory", "monolithic kernel", "not", "On-Demand Self-Service", "Broad Network Access",
          "Location-Independent Resource Pooling", "Rapid Elasticity", "Measured Service", "New", "Ready", "Running",
          "Waiting/Blocked", "Terminated", "Process", "Thread", "non-preemptive", "Convoy Effect", "Optimal Page Replacement",
          "predict", "Time Quantum", "Mutual Exclusion", "Hold and Wait", "No Preemption", "Circular Wait", "avoidance",
          "safe state", "preemption", "Paging", "swapping/paging", "3:1", "cache", "Belady's Anomaly", "Optimal", "future",
          "Internal Fragmentation", "External Fragmentation", "compaction", "Thrashing", "Working Set", "buff/cache",
          "16-bit addressing", "64 KB", "4 GB", "metadata", "not store the filename", "keystrokes", "screen redraw",
          "offline processing", "web browser", "user utility", "mail", "proxy", "application", "virtual", "blade", "policy",
          "file", "Botnet", "Physical", "Data Link", "Network", "Transport", "Session", "Presentation", "Application",
          "Bits", "Frames", "Packets", "Segments", "Datagrams", "Data", "3-way handshake", "Discover", "Offer", "Request",
          "Acknowledge", "right to left", "NAT", "Trunk Port", "802.1Q tagging", "MQTT", "CoAP", "TCP", "UDP", "interference",
          "switch", "MAC addresses", "ff:ff:ff:ff:ff:ff", "overlap", "IP Address", "Subnet Mask", "Default Gateway",
          "DNS Server", "5 GHz", "bandwidth", "low network bandwidth", "ICMP", "TTL", "tracert", "ps", "top", "htop", "kill",
          "df", "du", "Read", "Write", "Execute", "chmod 755", "w", "uname -a", "pipe", "CName", "wlbnginx.czu.cz", "WHOIS",
          "Ministerstvo vnitra CR", "ping -l", "ping -s", "4 bytes", "10101100", "157", "5", "3.67 ms"
        ];
        
        blurWords.forEach(w => {{
          const regex = new RegExp('\\\\b(' + w.replace(/[-\\/\\\\^$*+?.()|[\\]{{}}]/g, '\\\\$&') + ')\\\\b', 'g');
          parsedAns = parsedAns.replace(regex, '<span class="blur-reveal">$1</span>');
        }});

        card.innerHTML = `
          <div class="q-summary-row" onclick="toggleExpandRow(this.parentNode)">
            <div class="q-mastery-btns" onclick="event.stopPropagation()">
              <button class="m-btn check ${{isMastered ? 'active' : ''}}" title="Mark Mastered" onclick="toggleMasteryState('${{hash}}', 'mastered')">✓</button>
              <button class="m-btn star ${{isReview ? 'active' : ''}}" title="Needs Review" onclick="toggleMasteryState('${{hash}}', 'review')">⭐</button>
            </div>
            <div class="q-title-wrap">
              <span class="q-badge">${{idx + 1}}</span>
              <span class="q-badge" style="background:rgba(34, 211, 238, 0.08); color:var(--accent2);">${{CAT_LABELS[q.cat] || q.cat}}</span>
              <span class="q-title-text">${{htmlEscape(q.q)}}</span>
            </div>
            <span class="q-arrow">▼</span>
          </div>
          <div class="q-details-row">
            <div class="q-desc-box"><strong>Question:</strong> ${{htmlEscape(q.q)}}</div>
            <div class="q-ans-box">
              <strong>Study Guide Answer:</strong><br>
              ${{parsedAns}}
            </div>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function filterCategory(cat, btn) {{
      checklistCategory = cat;
      document.querySelectorAll('#checklist-category-filters .filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderChecklist();
    }}

    function handleSearch() {{
      renderChecklist();
    }}

    // ════════════════════════════════════════════════════════════════
    // FLASHCARDS VIEW LOGIC
    // ════════════════════════════════════════════════════════════════
    let fcList = [];
    let fcIndex = 0;
    let fcFlipped = false;
    let fcRatings = JSON.parse(localStorage.getItem('oscn_ratings') || '{{}}');

    function initFlashcards() {{
      const cat = document.getElementById('fc-category-select').value;
      if (cat === 'All') {{
        fcList = [...DATABASE];
      }} else if (cat === 'Weak') {{
        fcList = DATABASE.filter(q => fcRatings[q.q] === 'weak');
      }} else {{
        fcList = DATABASE.filter(q => q.cat === cat);
      }}
      
      fcIndex = 0;
      fcFlipped = false;
      document.getElementById('fc-card-body').classList.remove('flipped');
      updateFlashcardView();
    }}

    function updateFlashcardView() {{
      const total = fcList.length;
      document.getElementById('fc-stat-total').textContent = total;
      
      // Update ratings stats
      const knownCount = DATABASE.filter(q => fcRatings[q.q] === 'known').length;
      const weakCount = DATABASE.filter(q => fcRatings[q.q] === 'weak').length;
      document.getElementById('fc-stat-known').textContent = knownCount;
      document.getElementById('fc-stat-weak').textContent = weakCount;

      const fill = document.getElementById('fc-progress-bar-fill');
      if (total === 0) {{
        fill.style.width = '0%';
        document.getElementById('fc-front-cat').textContent = 'Empty';
        document.getElementById('fc-front-q').textContent = 'No cards match selected criteria.';
        document.getElementById('fc-back-cat').textContent = 'Empty';
        document.getElementById('fc-back-a').innerHTML = 'Select a different category or rate more cards.';
        return;
      }}
      
      fill.style.width = `${{((fcIndex + 1) / total) * 100}}%`;
      const q = fcList[fcIndex];
      document.getElementById('fc-front-cat').textContent = CAT_LABELS[q.cat] || q.cat;
      document.getElementById('fc-front-q').innerHTML = q.q;
      document.getElementById('fc-back-cat').textContent = CAT_LABELS[q.cat] || q.cat;
      
      // Wrap answers with red/green highlights for card keywords
      let parsed = q.desc;
      const highlightKeys = ["CPU time", "RAM", "HDD/SSD", "Kernel", "File System", "Programming Language", "User Interface (UI)", "API", "Cooperative", "Preemptive", "timer interrupts", "3:1", "page files", "swap files", "Type 1", "Type 2", "Copyleft", "Permissive", "EEPROM", "NAND flash", "1991", "Linus Torvalds", "not derived", "DORA", "distributed database", "right to left", "NAT", "Port 22", "ping", "traceroute", "tracert", "ICMP", "TCP", "UDP", "3-way handshake", "SYN", "SYN-ACK", "ACK", "MQTT", "CoAP", "Frame", "Packet", "Segment", "Bits", "VLAN tag", "4 bytes", "10101100", "157", "5", "3.67 ms"];
      highlightKeys.forEach(k => {{
        const r = new RegExp('\\\\b(' + k + ')\\\\b', 'gi');
        parsed = parsed.replace(r, '<strong style="color:var(--accent2);">$1</strong>');
      }});
      
      document.getElementById('fc-back-a').innerHTML = parsed;
    }}

    function flipCard() {{
      if (fcList.length === 0) return;
      fcFlipped = !fcFlipped;
      document.getElementById('fc-card-body').classList.toggle('flipped', fcFlipped);
    }}

    function nextCard(e) {{
      if (e) e.stopPropagation();
      if (fcList.length === 0) return;
      fcIndex = (fcIndex + 1) % fcList.length;
      fcFlipped = false;
      document.getElementById('fc-card-body').classList.remove('flipped');
      setTimeout(updateFlashcardView, 150);
    }}

    function prevCard(e) {{
      if (e) e.stopPropagation();
      if (fcList.length === 0) return;
      fcIndex = (fcIndex - 1 + fcList.length) % fcList.length;
      fcFlipped = false;
      document.getElementById('fc-card-body').classList.remove('flipped');
      setTimeout(updateFlashcardView, 150);
    }}

    function rateCard(rating, e) {{
      if (e) e.stopPropagation();
      if (fcList.length === 0) return;
      const q = fcList[fcIndex];
      fcRatings[q.q] = rating;
      localStorage.setItem('oscn_ratings', JSON.stringify(fcRatings));
      
      // Update checklist state sync
      const hash = getQHash(q.q);
      if (rating === 'known' && !masteredIds.includes(hash)) {{
        masteredIds.push(hash);
        const rIdx = reviewIds.indexOf(hash);
        if (rIdx > -1) reviewIds.splice(rIdx, 1);
        saveChecklistProgress();
      }} else if (rating === 'weak' && !reviewIds.includes(hash)) {{
        reviewIds.push(hash);
        const mIdx = masteredIds.indexOf(hash);
        if (mIdx > -1) masteredIds.splice(mIdx, 1);
        saveChecklistProgress();
      }}
      
      nextCard();
    }}

    function shuffleFlashcards() {{
      for (let i = fcList.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [fcList[i], fcList[j]] = [fcList[j], fcList[i]];
      }}
      fcIndex = 0;
      fcFlipped = false;
      document.getElementById('fc-card-body').classList.remove('flipped');
      updateFlashcardView();
    }}

    // Keybindings for flashcards
    document.addEventListener('keydown', e => {{
      const pane = document.getElementById('pane-flashcards');
      if (pane.classList.contains('active')) {{
        if (e.code === 'Space') {{
          e.preventDefault();
          flipCard();
        }} else if (e.code === 'ArrowRight') {{
          nextCard();
        }} else if (e.code === 'ArrowLeft') {{
          prevCard();
        }} else if (e.code === 'Digit1' || e.code === 'Numpad1') {{
          rateCard('weak');
        }} else if (e.code === 'Digit2' || e.code === 'Numpad2') {{
          rateCard('known');
        }} else if (e.key === 'r' || e.key === 'R') {{
          shuffleFlashcards();
        }}
      }}
    }});

    // ════════════════════════════════════════════════════════════════
    // MEMORIZE VIEW (AUDIO)
    // ════════════════════════════════════════════════════════════════
    function changeOSCNAudioVoice() {{
      const select = document.getElementById('oscn-audio-voice');
      const player = document.getElementById('oscn-audio-player');
      const source = document.getElementById('oscn-audio-source');
      const download = document.getElementById('oscn-audio-download');
      
      const val = select.value;
      source.src = val;
      download.href = val;
      player.load();
    }}

    // Browser TTS Narrator implementation
    const TTS_TRACKS = [
      {{ title: "OS Purpose & Resources", text: "Track 1. The Operating System controls and assigns system resources: CPU time, operating memory or RAM, and local storage space or HDD and SSD. It acts as a bridge between the user or applications and the hardware, and provides APIs for user programs." }},
      {{ title: "5 Elements of a Modern OS", text: "Track 2. A modern OS is composed of 5 elements. One: Kernel, which links applications to the hardware. Two: File System, which organizes data on local storage. Three: Programming Language used to write the OS. Four: User Interface, which is GUI or CLI. Five: API, which lets programs communicate." }},
      {{ title: "Cooperative vs. Preemptive Multitasking", text: "Track 3. Cooperative multitasking relies on applications to voluntarily yield CPU control back to the OS. One crashed program freezes the entire system. Preemptive multitasking allows the OS to forcibly reclaim the CPU using timer interrupts. misbehaving programs can be terminated gracefully." }},
      {{ title: "Desktop vs. Mobile OS Design", text: "Track 4. Mobile operating systems are designed for battery-operated devices, use touchscreens as primary interfaces, handle screen orientation changes, restrict background processes to save power, and implement strict sandboxing." }},
      {{ title: "Type 1 vs. Type 2 Hypervisors", text: "Track 5. Type 1 bare-metal hypervisors run directly on the physical hardware, offering high efficiency and security. Examples include VMware ESXi. Type 2 hosted hypervisors run as applications on top of a host OS, adding virtual overhead, like VirtualBox." }},
      {{ title: "Open Source Licenses: Copyleft vs. Permissive", text: "Track 6. Copyleft licenses like the GPL require any modified or derivative software to be open-source under the exact same terms. Permissive licenses like MIT or Apache allow users to modify, redistribute, and even close the source code for commercial use." }},
      {{ title: "BIOS Location and Role", text: "Track 7. The BIOS initializes and tests system hardware components during the boot POST and loads the bootloader. It is physically stored in non-volatile EEPROM or NAND flash memory on the motherboard." }},
      {{ title: "Linux Kernel Definition & History", text: "Track 8. Linux is a free, open-source monolithic kernel written from scratch by Linus Torvalds in 1991. It is Unix-like but not derived from original Unix code. It handles scheduling, memory, and devices." }},
      {{ title: "Cloud Computing & 5 Characteristics", text: "Track 9. Cloud computing delivers services over the internet. Its 5 characteristics are: On-Demand Self-Service, Broad Network Access, Location-Independent Resource Pooling, Rapid Elasticity, and Measured Service." }},
      {{ title: "5 Process States & Transitions", text: "Track 10. The five process states are: New, Ready, Running, Waiting, and Terminated. A key transition is Running to Ready, which is triggered by a timer interrupt slice." }},
      {{ title: "Process vs. Thread", text: "Track 11. A process is an independent program in execution with its own address space, memory, and PID. Context switching is expensive. A thread is a lightweight execution unit within a process, sharing its memory space and PID." }},
      {{ title: "First-Come, First-Served (FCFS) Scheduling", text: "Track 12. FCFS is a non-preemptive scheduling algorithm where processes run in arrival order. The Convoy Effect occurs when short processes wait behind a single, long CPU-bound process, spiking average wait times." }},
      {{ title: "Shortest Job First (SJF) Scheduling", text: "Track 13. SJF scheduling runs the process with the shortest next CPU burst. It is optimal for average wait times, but future burst durations cannot be predicted, causing starvation." }},
      {{ title: "Round Robin (RR) Scheduling", text: "Track 14. Round Robin assigns a small time slice or quantum Q. If Q is too small, context-switch overhead increases. If Q is too large, it behaves like FCFS." }},
      {{ title: "4 Deadlock Conditions", text: "Track 15. The 4 deadlock conditions are: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. All four must hold simultaneously for a deadlock to occur." }},
      {{ title: "Banker's Algorithm", text: "Track 16. The Banker's Algorithm is a deadlock avoidance algorithm. The OS simulates resource allocation and only grants resources if the system remains in a safe state." }},
      {{ title: "Deadlock Prevention vs. Recovery", text: "Track 17. Deadlock prevention structurally breaks at least one of the 4 conditions. Recovery allows deadlocks but resolves them by terminating processes or forcing resource preemption." }},
      {{ title: "Virtual Memory & Paging Principle", text: "Track 18. Virtual memory uses disk space to simulate RAM. The Memory Management Unit translates virtual to physical addresses. Disk access triggers a page fault, prompting the OS to load pages into frames." }},
      {{ title: "Swapping vs. Paging", text: "Track 19. Swapping moves an entire process between RAM and disk. Paging moves fixed-size page blocks. The recommended swap-to-RAM ratio is 3 to 1." }},
      {{ title: "Translation Lookaside Buffer (TLB)", text: "Track 20. The TLB is a high-speed hardware cache in the MMU storing recent address translations, preventing performance loss from double memory lookups." }}
    ];

    let ttsIndex = 0;
    let ttsPlaying = false;
    let ttsPaused = false;
    let wakeLock = null;

    async function requestWakeLock() {{
      try {{
        if ('wakeLock' in navigator) {{
          wakeLock = await navigator.wakeLock.request('screen');
        }}
      }} catch (e) {{}}
    }}

    function releaseWakeLock() {{
      if (wakeLock) {{
        wakeLock.release();
        wakeLock = null;
      }}
    }}

    function buildTTSPlaylist() {{
      const container = document.getElementById('tts-playlist-items-container');
      container.innerHTML = TTS_TRACKS.map((t, idx) => `
        <div class="cmd-item" id="tts-track-${{idx}}" onclick="jumpToTTSTrack(${{idx}})" style="cursor:pointer; padding: 6px 12px; border-radius: 6px; background:var(--surface);">
          <span class="cmd-name" style="color:var(--text-muted); font-family:var(--mono);">${{idx+1}}</span>
          <span class="cmd-desc">${{t.title}}</span>
        </div>
      `).join('');
    }}

    function loadSystemVoices() {{
      const select = document.getElementById('tts-voice-select');
      const voices = speechSynthesis.getVoices();
      select.innerHTML = '<option value="">Default System Voice</option>';
      
      voices.filter(v => v.lang.startsWith('en')).forEach(v => {{
        const opt = document.createElement('option');
        opt.value = v.name;
        opt.textContent = `${{v.name}} (${{v.lang}})`;
        select.appendChild(opt);
      }});
    }}
    speechSynthesis.addEventListener('voiceschanged', loadSystemVoices);

    function playTTSPlaylist() {{
      ttsPlaying = true;
      ttsPaused = false;
      document.getElementById('tts-play-btn').disabled = true;
      document.getElementById('tts-pause-btn').disabled = false;
      document.getElementById('tts-pause-btn').textContent = '⏸ Pause';
      
      requestWakeLock();
      speakTTSCurrentTrack();
    }}

    function speakTTSCurrentTrack() {{
      if (!ttsPlaying) return;
      
      // Update playlist selection class
      document.querySelectorAll('#tts-playlist-items-container .cmd-item').forEach((el, idx) => {{
        el.style.borderColor = idx === ttsIndex ? 'var(--accent2)' : 'transparent';
        el.style.background = idx === ttsIndex ? 'rgba(34,211,238,0.06)' : 'var(--surface)';
      }});
      
      const track = TTS_TRACKS[ttsIndex];
      document.getElementById('tts-playlist-counter').textContent = `${{ttsIndex + 1}} / 20`;
      document.getElementById('tts-now-playing-panel').innerHTML = `
        <span style="color:var(--accent2); font-weight:800;">Now Reading:</span> <span style="font-weight:700;">Track ${{ttsIndex+1}} - ${{track.title}}</span><br>
        <span style="color:var(--text-muted); font-size:0.75rem;">"${{track.text}}"</span>
      `;
      
      speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(track.text);
      const speed = parseFloat(document.getElementById('tts-speed-select').value) || 0.85;
      const voiceName = document.getElementById('tts-voice-select').value;
      
      utterance.rate = speed;
      if (voiceName) {{
        const voices = speechSynthesis.getVoices();
        const selected = voices.find(v => v.name === voiceName);
        if (selected) utterance.voice = selected;
      }}
      
      utterance.onend = () => {{
        if (ttsPlaying && !ttsPaused) {{
          ttsIndex++;
          if (ttsIndex < TTS_TRACKS.length) {{
            setTimeout(speakTTSCurrentTrack, 600);
          }} else {{
            stopTTSPlaylist();
          }}
        }}
      }};
      
      utterance.onerror = () => {{
        if (ttsPlaying && !ttsPaused) {{
          ttsIndex++;
          if (ttsIndex < TTS_TRACKS.length) {{
            setTimeout(speakTTSCurrentTrack, 600);
          }} else {{
            stopTTSPlaylist();
          }}
        }}
      }};
      
      speechSynthesis.speak(utterance);
    }}

    function pauseTTSPlaylist() {{
      if (!ttsPlaying) return;
      if (ttsPaused) {{
        // Resume
        speechSynthesis.resume();
        ttsPaused = false;
        requestWakeLock();
        document.getElementById('tts-pause-btn').textContent = '⏸ Pause';
        document.getElementById('tts-playlist-status').textContent = 'Playing...';
      }} else {{
        // Pause
        speechSynthesis.pause();
        ttsPaused = true;
        releaseWakeLock();
        document.getElementById('tts-pause-btn').textContent = '▶ Resume';
        document.getElementById('tts-playlist-status').textContent = 'Paused';
      }}
    }}

    function stopTTSPlaylist() {{
      ttsPlaying = false;
      ttsPaused = false;
      speechSynthesis.cancel();
      releaseWakeLock();
      
      document.getElementById('tts-play-btn').disabled = false;
      document.getElementById('tts-pause-btn').disabled = true;
      document.getElementById('tts-pause-btn').textContent = '⏸ Pause';
      document.getElementById('tts-playlist-status').textContent = 'Stopped.';
      document.getElementById('tts-playlist-counter').textContent = '0 / 20';
      document.getElementById('tts-now-playing-panel').innerHTML = '<span style="color:var(--text-muted)">Playlist not active. Press Play All to start reading.</span>';
      
      document.querySelectorAll('#tts-playlist-items-container .cmd-item').forEach(el => {{
        el.style.borderColor = 'transparent';
        el.style.background = 'var(--surface)';
      }});
      ttsIndex = 0;
    }}

    function jumpToTTSTrack(idx) {{
      ttsIndex = idx;
      ttsPlaying = true;
      ttsPaused = false;
      document.getElementById('tts-play-btn').disabled = true;
      document.getElementById('tts-pause-btn').disabled = false;
      document.getElementById('tts-pause-btn').textContent = '⏸ Pause';
      
      requestWakeLock();
      speakTTSCurrentTrack();
    }}

    function updateTTSSpeed() {{
      if (ttsPlaying && !ttsPaused) {{
        speakTTSCurrentTrack();
      }}
    }}

    // Bind wake lock to pre-recorded player too
    document.getElementById('oscn-audio-player').addEventListener('play', requestWakeLock);
    document.getElementById('oscn-audio-player').addEventListener('pause', releaseWakeLock);
    document.getElementById('oscn-audio-player').addEventListener('ended', releaseWakeLock);


    // ════════════════════════════════════════════════════════════════
    // TIMED MOCK EXAM
    // ════════════════════════════════════════════════════════════════
    let examQuestions = [];
    let examActiveIdx = 0;
    let examAnswers = {{}}; // idx -> array of selected option indexes
    let examTimerSecs = 1800; // 30 minutes
    let examTimerInterval = null;

    function startExam() {{
      const topic = document.getElementById('exam-topic-select').value;
      let pool = [...DATABASE];
      if (topic !== 'All') {{
        pool = pool.filter(q => q.cat === topic);
      }}
      
      // Shuffle pool
      for (let i = pool.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [pool[i], pool[j]] = [pool[j], pool[i]];
      }}
      
      examQuestions = pool.slice(0, Math.min(30, pool.length));
      examActiveIdx = 0;
      examAnswers = {{}};
      examTimerSecs = 1800;
      
      document.getElementById('exam-start-state').style.display = 'none';
      document.getElementById('exam-results-state').style.display = 'none';
      document.getElementById('exam-run-state').style.display = 'block';
      
      renderExamTracker();
      renderExamQuestion();
      startExamTimer();
    }}

    function startExamTimer() {{
      if (examTimerInterval) clearInterval(examTimerInterval);
      examTimerInterval = setInterval(() => {{
        if (examTimerSecs > 0) {{
          examTimerSecs--;
          const m = Math.floor(examTimerSecs / 60);
          const s = examTimerSecs % 60;
          document.getElementById('exam-timer-val').textContent = `${{String(m).padStart(2,'0')}}:${{String(s).padStart(2,'0')}}`;
          if (examTimerSecs < 180) {{
            document.getElementById('exam-timer').style.color = 'var(--red)';
            document.getElementById('exam-timer').style.borderColor = 'var(--red)';
          }} else {{
            document.getElementById('exam-timer').style.color = 'var(--accent)';
            document.getElementById('exam-timer').style.borderColor = 'rgba(249, 115, 22, 0.2)';
          }}
        }} else {{
          clearInterval(examTimerInterval);
          alert('Time is up! Submitting your exam.');
          submitExam();
        }}
      }}, 1000);
    }}

    function renderExamTracker() {{
      const container = document.getElementById('exam-tracker');
      container.innerHTML = '';
      
      examQuestions.forEach((_, idx) => {{
        const dot = document.createElement('div');
        const isAnswered = examAnswers[idx] !== undefined && examAnswers[idx].length > 0;
        dot.className = `tracker-dot ${{idx === examActiveIdx ? 'active' : ''}} ${{isAnswered ? 'answered' : ''}}`;
        dot.textContent = idx + 1;
        dot.onclick = () => jumpToQuestion(idx);
        container.appendChild(dot);
      }});
    }}

    function renderExamQuestion() {{
      const q = examQuestions[examActiveIdx];
      const container = document.getElementById('exam-q-box');
      container.innerHTML = '';
      
      document.getElementById('exam-subheading').textContent = `Question ${{examActiveIdx + 1}} of ${{examQuestions.length}} (${{q.cat}})`
      
      const isMulti = q.answers.length > 1;
      
      const title = document.createElement('div');
      title.className = 'exam-q-title';
      title.innerHTML = `
        <span class="exam-q-num">Q${{examActiveIdx + 1}}</span>
        <span>${{htmlEscape(q.q)}}</span>
      `;
      container.appendChild(title);
      
      if (isMulti) {{
        const warning = document.createElement('div');
        warning.style.cssText = 'color:var(--yellow); font-size:0.75rem; font-weight:700; margin:-0.75rem 0 1.25rem 2.8rem;';
        warning.textContent = '⚠️ SELECT ALL OPTIONS THAT APPLY (Multiple correct answers)';
        container.appendChild(warning);
      }}

      const optsBox = document.createElement('div');
      optsBox.className = 'exam-opts';
      
      const userSels = examAnswers[examActiveIdx] || [];
      
      q.options.forEach((opt, oidx) => {{
        const row = document.createElement('div');
        const isSelected = userSels.includes(oidx);
        row.className = `exam-opt ${{isSelected ? 'selected' : ''}}`;
        row.onclick = () => toggleExamOption(oidx, isMulti);
        
        const boxClass = isMulti ? 'exam-check-box' : 'exam-radio-box';
        row.innerHTML = `
          <div class="${{boxClass}}"></div>
          <span>${{htmlEscape(opt)}}</span>
        `;
        optsBox.appendChild(row);
      }});
      container.appendChild(optsBox);
      
      // Update buttons
      document.getElementById('exam-prev-btn').disabled = examActiveIdx === 0;
      document.getElementById('exam-next-btn').disabled = examActiveIdx === examQuestions.length - 1;
    }}

    function toggleExamOption(oidx, isMulti) {{
      if (!examAnswers[examActiveIdx]) {{
        examAnswers[examActiveIdx] = [];
      }}
      
      const list = examAnswers[examActiveIdx];
      if (isMulti) {{
        const pos = list.indexOf(oidx);
        if (pos > -1) list.splice(pos, 1);
        else list.push(oidx);
      }} else {{
        examAnswers[examActiveIdx] = [oidx];
      }}
      
      renderExamQuestion();
      renderExamTracker();
    }}

    function examPrev() {{
      if (examActiveIdx > 0) {{
        examActiveIdx--;
        renderExamQuestion();
        renderExamTracker();
      }}
    }}

    function examNext() {{
      if (examActiveIdx < examQuestions.length - 1) {{
        examActiveIdx++;
        renderExamQuestion();
        renderExamTracker();
      }}
    }}

    function jumpToQuestion(idx) {{
      examActiveIdx = idx;
      renderExamQuestion();
      renderExamTracker();
    }}

    function confirmSubmitExam() {{
      const answered = Object.keys(examAnswers).filter(k => examAnswers[k].length > 0).length;
      const total = examQuestions.length;
      if (answered < total) {{
        if (!confirm(`You have only answered ${{answered}} of ${{total}} questions. Are you sure you want to submit?`)) return;
      }} else {{
        if (!confirm('Are you sure you want to submit your exam for grading?')) return;
      }}
      submitExam();
    }}

    function submitExam() {{
      if (examTimerInterval) clearInterval(examTimerInterval);
      document.getElementById('exam-run-state').style.display = 'none';
      document.getElementById('exam-results-state').style.display = 'block';
      
      let score = 0;
      let reviewHtml = '';
      
      // Category stats tracker
      const catStats = {{}};
      
      examQuestions.forEach((q, idx) => {{
        const userSels = examAnswers[idx] || [];
        const correctTexts = q.answers;
        
        // Map user selected indexes to option texts
        const userTexts = userSels.map(o => q.options[o]);
        
        // Evaluate correctness
        const isCorrect = userTexts.length === correctTexts.length && userTexts.every(t => correctTexts.includes(t));
        if (isCorrect) score++;
        
        // Category diagnostics
        if (!catStats[q.cat]) catStats[q.cat] = {{ total: 0, correct: 0 }};
        catStats[q.cat].total++;
        if (isCorrect) catStats[q.cat].correct++;
        
        // Build review card
        let optListHtml = '';
        q.options.forEach((opt, oidx) => {{
          const isUserSel = userSels.includes(oidx);
          const isCorrectOpt = correctTexts.includes(opt);
          
          let cl = '';
          if (isUserSel && isCorrectOpt) cl = 'selected-correct';
          else if (isUserSel && !isCorrectOpt) cl = 'selected-wrong';
          else if (!isUserSel && isCorrectOpt) cl = 'missed';
          
          optListHtml += `<li class="review-opt-li ${{cl}}">${{htmlEscape(opt)}}</li>`;
        }});
        
        reviewHtml += `
          <div class="review-q-card ${{isCorrect ? 'correct' : 'wrong'}}">
            <div class="review-header">
              <span>Question ${{idx+1}} (${{q.cat}})</span>
              <span class="review-outcome-text ${{isCorrect ? 'correct' : 'wrong'}}">${{isCorrect ? '✓ CORRECT' : '✗ INCORRECT'}}</span>
            </div>
            <div class="review-q-txt">${{htmlEscape(q.q)}}</div>
            <ul class="review-opts">
              ${{optListHtml}}
            </ul>
            <div class="review-desc">
              <strong>Study Detail:</strong> ${{q.desc || 'No detail available.'}}
            </div>
          </div>
        `;
      }});
      
      const pct = Math.round((score / examQuestions.length) * 100) || 0;
      const isPassed = pct >= 60;
      
      document.getElementById('results-score-text').textContent = `${{score}} / ${{examQuestions.length}}`;
      document.getElementById('results-pct-text').textContent = `${{pct}}%`;
      
      const stroke = document.getElementById('results-stroke-fill');
      // perimeter of r=58 is 364.4
      stroke.style.strokeDashoffset = 364.4 - (pct / 100) * 364.4;
      
      const outcome = document.getElementById('results-outcome');
      outcome.textContent = isPassed ? 'PASSED' : 'FAILED';
      outcome.className = `results-outcome ${{isPassed ? 'pass' : 'fail'}}`;
      
      // Populate category diagnostic bars
      const barsContainer = document.getElementById('results-category-bars');
      barsContainer.innerHTML = '';
      
      Object.keys(catStats).forEach(cat => {{
        const stats = catStats[cat];
        const catPct = Math.round((stats.correct / stats.total) * 100) || 0;
        
        const row = document.createElement('div');
        row.className = 'diag-bar-row';
        row.innerHTML = `
          <div class="diag-bar-label">${{cat}}</div>
          <div class="diag-bar-track">
            <div class="diag-bar-fill" style="width: ${{catPct}}%;"></div>
          </div>
          <div class="diag-bar-val">${{catPct}}%</div>
        `;
        barsContainer.appendChild(row);
      }});
      
      document.getElementById('results-review-list').innerHTML = reviewHtml;
    }}

    function restartExam() {{
      document.getElementById('exam-start-state').style.display = 'block';
      document.getElementById('exam-run-state').style.display = 'none';
      document.getElementById('exam-results-state').style.display = 'none';
    }}


    // ════════════════════════════════════════════════════════════════
    // SANDBOXES VIEW SWITCHER
    // ════════════════════════════════════════════════════════════════
    function switchSandboxTab(id, btn) {{
      document.querySelectorAll('#pane-tools .tab-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#pane-tools .tab-btn').forEach(b => b.classList.remove('active'));
      
      const pane = document.getElementById(id);
      if (pane) pane.classList.add('active');
      btn.classList.add('active');
      
      if (id === 'sand-terminal') {{
        initTerminalChallenge();
      }}
    }}

    // ════════════════════════════════════════════════════════════════
    // CPU SCHEDULING SIMULATOR
    // ════════════════════════════════════════════════════════════════
    const G_COLORS = ['#22d3ee', '#f97316', '#a78bfa', '#4ade80', '#f87171', '#fbbf24', '#f472b6', '#60a5fa'];
    function parseProcs() {{
      return document.getElementById('cpu-procs').value.trim().split('\\n').filter(l => l.trim()).map(l => {{
        const parts = l.split(',');
        return {{
          name: parts[0]?.trim() || 'P',
          arrival: parseInt(parts[1] || 0),
          burst: parseInt(parts[2] || 1)
        }};
      }});
    }}

    function runCPU() {{
      const procs = parseProcs();
      const algo = document.getElementById('cpu-algo').value;
      const q = parseInt(document.getElementById('cpu-quantum').value) || 2;
      
      if (!procs.length) {{
        document.getElementById('cpu-result').innerHTML = '<span style="color:var(--red);">No processes entered.</span>';
        return;
      }}
      
      let timeline = [];
      let result = [];
      
      if (algo === 'fcfs') {{
        result = simFCFS(procs, timeline);
      }} else if (algo === 'sjf') {{
        result = simSJF(procs, timeline);
      }} else {{
        result = simRR(procs, q, timeline);
      }}
      
      renderCPUResult(result, timeline, algo, q);
    }}

    function simFCFS(procs, tl) {{
      const ps = [...procs].sort((a,b) => a.arrival - b.arrival);
      let t = 0;
      let res = [];
      ps.forEach((p, idx) => {{
        if (t < p.arrival) t = p.arrival;
        tl.push({{ name: p.name, start: t, end: t + p.burst, ci: idx }});
        const wt = t - p.arrival;
        const tat = wt + p.burst;
        res.push({{ name: p.name, arrival: p.arrival, burst: p.burst, start: t, finish: t + p.burst, wt, tat }});
        t += p.burst;
      }});
      return res;
    }}

    function simSJF(procs, tl) {{
      const ps = ps = procs.map(p => ({{ ...p, done: false }}));
      let t = 0;
      let res = [];
      let completed = 0;
      let idx = 0;
      while (completed < ps.length) {{
        const avail = ps.filter(p => !p.done && p.arrival <= t);
        if (!avail.length) {{
          t++;
          continue;
        }}
        avail.sort((a,b) => a.burst - b.burst);
        const p = avail[0];
        tl.push({{ name: p.name, start: t, end: t + p.burst, ci: idx++ }});
        const wt = t - p.arrival;
        const tat = wt + p.burst;
        res.push({{ name: p.name, arrival: p.arrival, burst: p.burst, start: t, finish: t + p.burst, wt, tat }});
        t += p.burst;
        p.done = true;
        completed++;
      }}
      return res;
    }}

    function simRR(procs, q, tl) {{
      const ps = procs.map(p => ({{ ...p, remaining: p.burst, firstRun: -1 }}));
      let t = 0;
      let queue = [];
      let done = [];
      let idx = 0;
      let arrived = new Set();
      
      ps.filter(p => p.arrival === 0).forEach(p => {{ queue.push(p); arrived.add(p.name); }});
      
      let guard = 0;
      while (done.length < ps.length && guard < 1000) {{
        guard++;
        if (!queue.length) {{
          t++;
          ps.filter(p2 => !arrived.has(p2.name) && p2.arrival <= t).forEach(p2 => {{ queue.push(p2); arrived.add(p2.name); }});
          continue;
        }}
        const p = queue.shift();
        if (p.firstRun === -1) p.firstRun = t;
        const run = Math.min(q, p.remaining);
        tl.push({{ name: p.name, start: t, end: t + run, ci: idx++ }});
        t += run;
        p.remaining -= run;
        
        ps.filter(p2 => !arrived.has(p2.name) && p2.arrival <= t).forEach(p2 => {{ queue.push(p2); arrived.add(p2.name); }});
        if (p.remaining > 0) {{
          queue.push(p);
        }} else {{
          done.push({{ name: p.name, arrival: p.arrival, burst: p.burst, start: p.firstRun, finish: t, wt: t - p.burst - p.arrival, tat: t - p.arrival }});
        }}
      }}
      return done;
    }}

    function renderCPUResult(result, tl, algo, q) {{
      const avgWT = result.reduce((s,r) => s + r.wt, 0) / result.length;
      const avgTAT = result.reduce((s,r) => s + r.tat, 0) / result.length;
      
      let html = `<div><span class="rl">Algorithm: </span><span class="rv">${{algo.toUpperCase()}}${{algo==='rr'?' (Q='+q+')':''}}</span></div>`;
      html += `<br><div style="color:var(--text-muted); font-size:0.7rem; font-family:var(--mono); margin-bottom:4px;">PID  ARR  BURST  WAIT  TURNAROUND</div>`;
      result.forEach(r => {{
        html += `<div><span class="rv">${{r.name.padEnd(4)}}</span><span class="rl">${{String(r.arrival).padStart(3)}}  ${{String(r.burst).padStart(5)}}</span>  <span class="ro">${{String(r.wt).padStart(4)}}</span>  <span class="rg">${{String(r.tat).padStart(10)}}</span></div>`;
      }});
      html += `<br><div><span class="rl">Average Waiting Time (WT): </span><span class="ro">${{avgWT.toFixed(2)}} ms</span></div>`;
      html += `<div><span class="rl">Average Turnaround (TAT): </span><span class="rg">${{avgTAT.toFixed(2)}} ms</span></div>`;
      
      document.getElementById('cpu-result').innerHTML = html;
      
      const g = document.getElementById('gantt');
      const gl = document.getElementById('g-labels');
      g.innerHTML = '';
      gl.innerHTML = '';
      
      const totalTime = tl[tl.length - 1].end - tl[0].start;
      tl.forEach((seg, i) => {{
        const w = ((seg.end - seg.start) / totalTime * 100) + '%';
        const s = document.createElement('div');
        s.className = 'g-seg';
        s.style.cssText = `width:${{w}}; background:${{G_COLORS[i%G_COLORS.length]}}22; color:${{G_COLORS[i%G_COLORS.length]}}; border-bottom:3px solid ${{G_COLORS[i%G_COLORS.length]}}`;
        s.textContent = seg.name;
        s.title = `${{seg.name}}: ${{seg.start}}→${{seg.end}}`;
        g.appendChild(s);
        
        const lbl = document.createElement('span');
        lbl.className = 'g-lbl';
        lbl.style.width = w;
        lbl.textContent = seg.start;
        gl.appendChild(lbl);
      }});
      
      const last = document.createElement('span');
      last.textContent = tl[tl.length - 1].end;
      last.style.marginLeft = 'auto';
      gl.appendChild(last);
      
      document.getElementById('gantt-wrap').style.display = 'block';
    }}

    // ════════════════════════════════════════════════════════════════
    // SUBNETTING CALCULATOR
    // ════════════════════════════════════════════════════════════════
    function runSubnet() {{
      const ipStr = document.getElementById('sub-ip').value.trim();
      const prefix = parseInt(document.getElementById('sub-prefix').value);
      const parts = ipStr.split('.').map(Number);
      
      if (parts.length !== 4 || parts.some(p => isNaN(p) || p < 0 || p > 255) || isNaN(prefix) || prefix < 1 || prefix > 32) {{
        document.getElementById('subnet-result').innerHTML = '<span style="color:var(--red)">Invalid IP address or CIDR mask prefix (1-32).</span>';
        return;
      }}
      
      const mask = (-1 << (32 - prefix)) >>> 0;
      const ipInt = ((parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]) >>> 0;
      const net = (ipInt & mask) >>> 0;
      const bcast = (net | (~mask >>> 0)) >>> 0;
      const first = (net + 1) >>> 0;
      const last = (bcast - 1) >>> 0;
      const hosts = Math.max(0, Math.pow(2, 32 - prefix) - 2);
      
      const subnetMask = [mask >>> 24, (mask >>> 16) & 0xff, (mask >>> 8) & 0xff, mask & 0xff].join('.');
      const toIP = n => [n >>> 24, (n >>> 16) & 0xff, (n >>> 8) & 0xff, n & 0xff].join('.');
      
      const fullBin = (ipInt >>> 0).toString(2).padStart(32, '0');
      const netBits = `<span style="color:var(--accent2); font-weight:700;">${{fullBin.slice(0, prefix)}}</span><span style="color:var(--accent); font-weight:700;">${{fullBin.slice(prefix)}}</span>`;
      
      document.getElementById('subnet-result').innerHTML = `
        <div><span class="rl">Network Address:  </span><span class="rv">${{toIP(net)}}</span></div>
        <div><span class="rl">Subnet Mask:      </span><span class="rv">${{subnetMask}}</span></div>
        <div><span class="rl">CIDR notation:    </span><span class="rv">/${{prefix}}</span></div>
        <div><span class="rl">Broadcast IP:     </span><span class="ro">${{toIP(bcast)}}</span></div>
        <div><span class="rl">First Usable IP:  </span><span class="rg">${{toIP(first)}}</span></div>
        <div><span class="rl">Last Usable IP:   </span><span class="rg">${{toIP(last)}}</span></div>
        <div><span class="rl">Usable Hosts:     </span><span class="rv">${{hosts.toLocaleString()}} (2^${{32 - prefix}} - 2)</span></div>
        <div style="margin-top:0.75rem;"><span class="rl">Binary IP Structure: </span>${{netBits}}</div>
        <div style="font-size:0.65rem; margin-top:2px;"><span style="color:var(--accent2);">■ network bits</span> <span style="color:var(--accent);">■ host bits</span></div>
      `;
    }}

    // ════════════════════════════════════════════════════════════════
    // PAGE REPLACEMENT SIMULATOR
    // ════════════════════════════════════════════════════════════════
    function runPage() {{
      const refStr = document.getElementById('page-ref').value.trim().split(/\\s+/).map(Number);
      const frames = parseInt(document.getElementById('page-frames').value);
      const algo = document.getElementById('page-algo').value;
      
      if (!refStr.length || refStr.some(isNaN)) {{
        document.getElementById('page-result').innerHTML = '<span style="color:var(--red);">Invalid page reference string.</span>';
        return;
      }}
      
      let mem = [];
      let faults = 0;
      let history = [];
      let faultFlags = [];
      
      if (algo === 'fifo') {{
        let queue = [];
        refStr.forEach(page => {{
          const fault = !mem.includes(page);
          if (fault) {{
            faults++;
            if (mem.length >= frames) {{
              const rem = queue.shift();
              mem = mem.filter(p => p !== rem);
            }}
            mem.push(page);
            queue.push(page);
          }}
          faultFlags.push(fault);
          history.push([...mem]);
        }});
      }} else {{
        refStr.forEach((page, t) => {{
          const fault = !mem.includes(page);
          if (fault) {{
            faults++;
            if (mem.length >= frames) {{
              let lruIdx = Infinity;
              let lruPage = mem[0];
              mem.forEach(p => {{
                const lu = refStr.slice(0, t).lastIndexOf(p);
                if (lu < lruIdx) {{
                  lruIdx = lu;
                  lruPage = p;
                }}
              }});
              mem = mem.filter(p => p !== lruPage);
            }}
            mem.push(page);
          }}
          faultFlags.push(fault);
          history.push([...mem]);
        }});
      }}
      
      const hitRate = (((refStr.length - faults) / refStr.length) * 100).toFixed(1);
      document.getElementById('page-result').innerHTML = `
        <div><span class="rl">Algorithm:     </span><span class="rv">${{algo.toUpperCase()}}</span></div>
        <div><span class="rl">Total Pages:   </span><span class="rv">${{refStr.length}}</span></div>
        <div><span class="rl">Page Faults:   </span><span class="ro">${{faults}}</span></div>
        <div><span class="rl">Hits:          </span><span class="rg">${{refStr.length - faults}}</span></div>
        <div><span class="rl">Hit Rate:      </span><span class="rg">${{hitRate}}%</span></div>
      `;
      
      const tw = document.getElementById('page-table-wrap');
      let tbl = `<div style="font-size:0.7rem; color:var(--text-muted); font-weight:700; margin-bottom:4px; text-transform:uppercase;">Simulation Matrix</div>
                 <table style="border-collapse:collapse; font-size:0.72rem; font-family:var(--mono);">
                 <tr style="border-bottom:1px solid var(--border-light);"><td style="padding:4px 8px; color:var(--text-muted);">Ref</td>`;
      refStr.forEach((p, i) => {{
        const bg = faultFlags[i] ? 'rgba(249,115,22,0.18)' : 'rgba(34,211,238,0.08)';
        tbl += `<td style="padding:4px 8px; background:${{bg}}; border:1px solid rgba(255,255,255,0.04); color:${{faultFlags[i] ? 'var(--accent)' : 'var(--accent2)'}}; font-weight:800;">${{p}}</td>`;
      }});
      tbl += '</tr>';
      
      for (let f = 0; f < frames; f++) {{
        tbl += `<tr><td style="padding:4px 8px; color:var(--text-muted);">F${{f+1}}</td>`;
        refStr.forEach((_, i) => {{
          const page = history[i][f] !== undefined ? history[i][f] : '·';
          tbl += `<td style="padding:4px 8px; border:1px solid rgba(255,255,255,0.04); text-align:center;">${{page}}</td>`;
        }});
        tbl += '</tr>';
      }}
      
      tbl += `<tr style="border-top:1px solid var(--border-light);"><td style="padding:4px 8px; color:var(--text-muted);">Fault</td>`;
      faultFlags.forEach(f => {{
        tbl += `<td style="padding:4px 8px; border:1px solid rgba(255,255,255,0.04); text-align:center; color:${{f ? 'var(--accent)' : 'var(--text-muted)'}};">${{f ? '✗' : '·'}}</td>`;
      }});
      tbl += '</tr></table>';
      
      tw.innerHTML = tbl;
      tw.style.display = 'block';
    }}

    // ════════════════════════════════════════════════════════════════
    // IP CONVERTER
    // ════════════════════════════════════════════════════════════════
    function decToBin() {{
      const ip = document.getElementById('d2b-input').value.trim();
      const parts = ip.split('.').map(Number);
      if (parts.length !== 4 || parts.some(p => isNaN(p) || p < 0 || p > 255)) {{
        document.getElementById('d2b-result').innerHTML = '<span style="color:var(--accent)">Invalid IP format (x.x.x.x)</span>';
        return;
      }}
      const binParts = parts.map(p => p.toString(2).padStart(8, '0'));
      let html = `<div><span class="rl">Decimal IP: </span><span class="rv">${{ip}}</span></div>`;
      binParts.forEach((b, i) => {{
        html += `<div><span class="rl">Octet ${{i+1}}: ${{parts[i].toString().padStart(3)}} → </span><span class="rv">${{b}}</span></div>`;
      }});
      html += `<div style="margin-top:6px; border-top:1px solid var(--border); padding-top:6px;"><span class="rl">Full Binary IP: </span><span class="rv" style="color:var(--accent);">${{binParts.join('.')}}</span></div>`;
      document.getElementById('d2b-result').innerHTML = html;
    }}

    function binToDec() {{
      const raw = document.getElementById('b2d-input').value.trim().replace(/\\s+/g, '.');
      const parts = raw.split('.');
      if (parts.length !== 4 || parts.some(p => !/^[01]{{8}}$/.test(p))) {{
        document.getElementById('b2d-result').innerHTML = '<span style="color:var(--accent)">Enter 4 binary octets separated by dots (e.g. 11000000.10101000...)</span>';
        return;
      }}
      const decParts = parts.map(p => parseInt(p, 2));
      let html = `<div><span class="rl">Binary IP: </span><span class="rv" style="font-size:0.75rem">${{raw}}</span></div>`;
      parts.forEach((b, i) => {{
        html += `<div><span class="rl">Octet ${{i+1}}: ${{b}} → </span><span class="rv">${{decParts[i]}}</span></div>`;
      }});
      html += `<div style="margin-top:6px; border-top:1px solid var(--border); padding-top:6px;"><span class="rl">Decimal IP: </span><span class="rv" style="color:var(--accent2);">${{decParts.join('.')}}</span></div>`;
      document.getElementById('b2d-result').innerHTML = html;
    }}


    // ════════════════════════════════════════════════════════════════
    // LINUX TERMINAL CHALLENGE GAME
    // ════════════════════════════════════════════════════════════════
    const TERM_CHALLENGES = [
      {{
        title: "Force Terminate a Process",
        desc: "A process with PID <strong>4892</strong> is hung and consuming 100% CPU. Write a Linux command to forcefully and immediately terminate it.",
        regex: /^kill\s+-9\s+4892$/,
        hint: "Use the kill command with the SIGKILL signal (-9) followed by the process ID.",
        solution: "kill -9 4892"
      }},
      {{
        title: "Set Executable Permissions",
        desc: "You need to make a script named <code>backup.sh</code> executable by all users (owner, group, and others), preserving read/write access. Use the numeric chmod syntax.",
        regex: /^chmod\s+755\s+backup\.sh$/,
        hint: "Permissions: Owner=7(rwx), Group=5(r-x), Others=5(r-x). Name: backup.sh",
        solution: "chmod 755 backup.sh"
      }},
      {{
        title: "Search for a Specific User's Log",
        desc: "Filter a file named <code>/var/log/auth.log</code> to display only lines containing the username <code>vokoun</code>.",
        regex: /^grep\s+["']?vokoun["']?\s+\/var\/log\/auth\.log$/,
        hint: "Use the grep command with target term 'vokoun' and target file path '/var/log/auth.log'.",
        solution: "grep vokoun /var/log/auth.log"
      }},
      {{
        title: "Check System Uptime and Users",
        desc: "Write the short, single-letter command that lists system load averages, uptime, and currently logged-in users.",
        regex: /^w$/,
        hint: "It is a single character command, the letter 'w'.",
        solution: "w"
      }},
      {{
        title: "Check Listening Socket Details",
        desc: "Write the modern command to show all listening TCP and UDP sockets with their port numbers and process IDs. Do NOT use netstat.",
        regex: /^ss\s+-tulpn$/,
        hint: "Use ss command with flags: -t(tcp), -u(udp), -l(listening), -p(process), -n(numeric).",
        solution: "ss -tulpn"
      }}
    ];

    let currentTermChallIdx = 0;
    let termHistory = [];

    function initTerminalChallenge() {{
      currentTermChallIdx = 0;
      termHistory = [
        "Welcome to the vokoun@ete2ae terminal sandbox!",
        "Complete all 5 challenges to prove Linux CLI mastery.",
        "--------------------------------------------------",
        ""
      ];
      renderTerminalState();
    }}

    function renderTerminalState() {{
      const chall = TERM_CHALLENGES[currentTermChallIdx];
      if (!chall) return;
      
      document.getElementById('term-challenge-progress').textContent = `Task ${{currentTermChallIdx + 1}} of 5`;
      document.getElementById('term-challenge-title').textContent = chall.title;
      document.getElementById('term-challenge-desc').innerHTML = chall.desc;
      document.getElementById('term-challenge-hint-box').style.display = 'none';
      document.getElementById('term-challenge-hint-txt').textContent = chall.hint;
      
      // Update terminal history log
      const histEl = document.getElementById('term-console-history');
      histEl.innerHTML = termHistory.join('<br>');
      
      const body = histEl.parentNode;
      body.scrollTop = body.scrollHeight;
    }}

    function handleTerminalKeyPress(e) {{
      if (e.key === 'Enter') {{
        const inputEl = document.getElementById('term-user-input');
        const val = inputEl.value.trim();
        if (!val) return;
        
        termHistory.push(`vokoun@ete2ae:~$ ${{htmlEscape(val)}}`);
        
        const chall = TERM_CHALLENGES[currentTermChallIdx];
        if (chall.regex.test(val)) {{
          termHistory.push(`<span style="color:var(--green)">✓ Correct! Command successfully completed.</span>`);
          termHistory.push("");
          currentTermChallIdx++;
          
          if (currentTermChallIdx < TERM_CHALLENGES.length) {{
            termHistory.push(`Loading Task ${{currentTermChallIdx + 1}}...`);
            setTimeout(renderTerminalState, 400);
          }} else {{
            termHistory.push(`<span style="color:var(--yellow); font-weight:800;">🎉 CONGRATULATIONS! You have completed all terminal challenges!</span>`);
            setTimeout(renderTerminalState, 400);
          }}
        }} else {{
          termHistory.push(`<span style="color:var(--red)">✗ Error: command not found or incorrect options. Try again.</span>`);
          termHistory.push("");
          renderTerminalState();
        }}
        inputEl.value = '';
      }}
    }}

    function showTerminalChallengeHint() {{
      document.getElementById('term-challenge-hint-box').style.display = 'block';
    }}

    function skipTerminalChallenge() {{
      const chall = TERM_CHALLENGES[currentTermChallIdx];
      termHistory.push(`vokoun@ete2ae:~$ [Skipped task]`);
      termHistory.push(`Correct command was: <code>${{chall.solution}}</code>`);
      termHistory.push("");
      currentTermChallIdx++;
      if (currentTermChallIdx < TERM_CHALLENGES.length) {{
        renderTerminalState();
      }} else {{
        termHistory.push(`<span style="color:var(--yellow)">Terminal sandbox finished. Restart to try again.</span>`);
        renderTerminalState();
      }}
    }}

    function resetTerminalChallenge() {{
      initTerminalChallenge();
    }}


    // ════════════════════════════════════════════════════════════════
    // DEFINITIONS MATCHER GAME
    // ════════════════════════════════════════════════════════════════
    const MATCH_ALL_PAIRS = [
      {{ term: 'Process', def: 'A running program with its own PID, virtual memory space, and resources.' }},
      {{ term: 'Thread', def: 'Lightweight execution unit within a process, sharing parent memory.' }},
      {{ term: 'Deadlock', def: 'State requiring Mutual Exclusion, Hold-and-Wait, No Preemption, Circular Wait.' }},
      {{ term: 'Virtual Memory', def: 'OS uses HDD/SSD space to simulate additional physical RAM.' }},
      {{ term: 'Swapping', def: 'Technique that transfers an ENTIRE process between RAM and disk.' }},
      {{ term: 'Paging', def: 'Moving fixed-size blocks (pages) between RAM and disk. Recommended ratio 3:1.' }},
      {{ term: 'Preemptive Multitasking', def: 'OS forcibly controls CPU time allocation using timer interrupts.' }},
      {{ term: 'NAT', def: 'Converts private IP to public IP at the router boundary for internet access.' }},
      {{ term: 'DNS', def: 'Distributed database resolving domains to IPs; read right-to-left.' }},
      {{ term: 'SSH', def: 'Encrypted remote access protocol using a secure channel on port 22.' }},
      {{ term: 'ICMP', def: 'L3 diagnostics protocol (ping/tracert) that has no port numbers.' }},
      {{ term: 'Public IP', def: 'Globally unique IP address assigned by ISP, visible on internet.' }},
      {{ term: 'Private IP', def: 'Local network IP (RFC 1918), non-routable on the public internet.' }},
      {{ term: 'BIOS', def: 'Motherboard firmware stored in EEPROM/NAND flash to test hardware at boot.' }},
      {{ term: 'FAT16', def: 'Older FS limited to 4 GB partition size due to 16-bit cluster addressing.' }},
      {{ term: 'Batch Processing', def: 'Executes grouped jobs offline without user interaction during execution.' }},
      {{ term: 'Kernel', def: 'Core OS component linking applications to hardware and allocating resources.' }},
      {{ term: 'SaaS', def: 'Cloud model delivering ready applications like Gmail or Office365.' }},
      {{ term: 'IaaS', def: 'Cloud model providing hardware, VMs and storage (e.g. AWS EC2).' }},
      {{ term: 'PaaS', def: 'Cloud model providing OS and runtimes for custom application deployment.' }},
      {{ term: 'Botnet', def: 'Malicious software network acting autonomously in batch-agent models.' }},
      {{ term: 'MQTT', def: 'IoT publish/subscribe protocol running over TCP, requires a broker.' }},
      {{ term: 'CoAP', def: 'IoT RESTful GET/POST protocol running over UDP, no broker needed.' }},
      {{ term: 'ARP', def: 'Address Resolution Protocol mapping IP addresses to local MAC addresses.' }}
    ];

    let matchPairs = [];
    let matchSelectedEl = null;
    let matchSelectedType = null;
    let matchSelectedIdx = null;
    let matchMatchedCount = 0;

    function shuffleArray(arr) {{
      for (let i = arr.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }}
    }}

    function initMatcher() {{
      const grid = document.getElementById('match-grid');
      grid.innerHTML = '';
      matchMatchedCount = 0;
      matchSelectedEl = null;
      matchSelectedType = null;
      matchSelectedIdx = null;
      updateMatcherProgress();
      
      // Select 8 random pairs
      const pool = [...MATCH_ALL_PAIRS];
      shuffleArray(pool);
      matchPairs = pool.slice(0, 8);
      
      // Separate terms and definitions, shuffle independently
      const termsList = matchPairs.map((p, idx) => ({{ term: p.term, idx }}));
      const defsList = matchPairs.map((p, idx) => ({{ def: p.def, idx }}));
      shuffleArray(termsList);
      shuffleArray(defsList);
      
      const leftCol = document.createElement('div');
      leftCol.style.cssText = 'display:flex; flex-direction:column; gap:6px;';
      const rightCol = document.createElement('div');
      rightCol.style.cssText = 'display:flex; flex-direction:column; gap:6px;';
      
      termsList.forEach(t => {{
        const el = document.createElement('div');
        el.className = 'match-card-item';
        el.textContent = t.term;
        el.onclick = () => selectMatcherItem(el, 'term', t.idx);
        leftCol.appendChild(el);
      }});
      
      defsList.forEach(d => {{
        const el = document.createElement('div');
        el.className = 'match-card-item';
        el.textContent = d.def;
        el.onclick = () => selectMatcherItem(el, 'def', d.idx);
        rightCol.appendChild(el);
      }});
      
      grid.appendChild(leftCol);
      grid.appendChild(rightCol);
    }}

    function selectMatcherItem(el, type, idx) {{
      if (el.classList.contains('matched')) return;
      
      // Clean selections of same type
      document.querySelectorAll(`#match-grid .match-card-item`).forEach(e => {{
        if (e.textContent === el.textContent) return; // ignore current
        // if same column, unselect
        const isTerm = MATCH_ALL_PAIRS.some(p => p.term === e.textContent);
        if ((type === 'term' && isTerm) || (type === 'def' && !isTerm)) {{
          e.classList.remove('selected');
        }}
      }});
      
      el.classList.add('selected');
      
      if (!matchSelectedEl) {{
        matchSelectedEl = el;
        matchSelectedType = type;
        matchSelectedIdx = idx;
        return;
      }}
      
      if (matchSelectedType === type) {{
        // Toggle selection
        matchSelectedEl.classList.remove('selected');
        matchSelectedEl = el;
        matchSelectedIdx = idx;
        return;
      }}
      
      // Compare
      if (matchSelectedIdx === idx) {{
        // Match!
        matchSelectedEl.classList.remove('selected');
        matchSelectedEl.classList.add('matched', 'glow');
        el.classList.remove('selected');
        el.classList.add('matched', 'glow');
        matchMatchedCount++;
        updateMatcherProgress();
        matchSelectedEl = null;
        matchSelectedType = null;
        matchSelectedIdx = null;
      }} else {{
        // Wrong
        const first = matchSelectedEl;
        first.classList.add('wrong');
        el.classList.add('wrong');
        setTimeout(() => {{
          first.classList.remove('wrong', 'selected');
          el.classList.remove('wrong', 'selected');
        }}, 400);
        matchSelectedEl = null;
        matchSelectedType = null;
        matchSelectedIdx = null;
      }}
    }}

    function updateMatcherProgress() {{
      const pct = Math.round((matchMatchedCount / 8) * 100) || 0;
      document.getElementById('mscore-text').textContent = `${{matchMatchedCount}} / 8 Matched`;
      document.getElementById('mscore-pct').textContent = `${{pct}}%`;
      document.getElementById('mscore-bar').style.width = `${{pct}}%`;
      
      if (matchMatchedCount === 8) {{
        setTimeout(() => {{
          alert('🎉 Congratulations! You matched all definitions successfully.');
        }}, 300);
      }}
    }}

    // INITIALIZATION
    window.onload = () => {{
      renderChecklist();
      updateOverallStats();
      initFlashcards();
      buildTTSPlaylist();
      loadSystemVoices();
      initMatcher();
    }};
  </script>
</body>
</html>"""

    # Format JSON strings
    db_json = json.dumps(DATABASE, indent=2)
    
    # Prepare Anki TSV block content
    # Replace values in the template using .replace to avoid curly brace conflicts
    full_html = html_template.replace('{{', '{').replace('}}', '}')
    full_html = full_html.replace('{database_json}', db_json)
    full_html = full_html.replace('{anki_tsv}', anki_tsv_content)
    
    # Save the file
    out_path = "d:/CZUU/OS_EXAM_SUITE/EXAM_MASTER_2H.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Successfully generated OS Master Guide at d:/CZUU/OS_EXAM_SUITE/EXAM_MASTER_2H.html")

if __name__ == '__main__':
    generate_html()
