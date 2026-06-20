# OS & Networks — ETE2AE Exam Prep Suite
**CZU Prague | Operating Systems & Computer Networks**

---

## 📦 Files

| File | Description |
|------|-------------|
| `index.html` | Main dashboard with interactive simulators and references |
| `smart_cram_cards.html` | 3D flip flashcard study app (67 cards) |
| `README.md` | This file |

---

## 🚀 Quick Start

1. Open `index.html` in any modern browser (Chrome, Firefox, Edge)
2. Use **Normal Mode** for full solver access; **Cram Mode** for focused revision
3. Click **Smart Cram Cards** (top-right) to study with `smart_cram_cards.html`

> No server required — all files are self-contained HTML with embedded JavaScript.

---

## 📚 Course Overview

**Course Code:** ETE2AE  
**Subject:** Operating Systems & Computer Networks  
**Program:** IT — CZU Prague  
**Assessment:** Written exam — theory + calculation/CLI problems

---

## 🗺 Topic Coverage

### Operating Systems:
#### 1. Process Management
- Processes, threads, scheduling algorithms (FCFS, SJF, Round Robin, Priority)
- Starvation, aging, context switches
- Mutexes, semaphores, race conditions, fork() system call

#### 2. Memory Management
- Paging, segmentation, virtual memory, translation lookaside buffer (TLB)
- Page replacement algorithms (FIFO, LRU, Optimal)
- Belady's Anomaly, thrashing, working set model, fragmentation (internal/external)

#### 3. File Systems & Resource Sharing
- FAT, NTFS, ext4, inodes, directory structures
- Deadlock conditions (Mutual exclusion, Hold-and-wait, No preemption, Circular wait)
- Banker's Algorithm (deadlock avoidance), deadlock prevention vs detection

#### 4. Linux Commands
- `ls`, `cd`, `cp`, `mv`, `rm`, `chmod`, `grep`, `ps`, `kill`, `top`/`htop`, `df`, `du`, `ping`, `netstat`/`ss`

### Computer Networks:
#### 1. OSI & TCP/IP Reference Models
- OSI 7 layers and functions (Physical, Data Link, Network, Transport, Session, Presentation, Application)
- TCP/IP 4 layers (Network Access, Internet, Transport, Application)
- Key protocols and PDUs (data units) per layer (Bits, Frames, Packets, Segments, Data)

#### 2. IP Addressing & Subnetting
- IPv4 addressing, subnet masks, CIDR notation
- Classful addressing (A, B, C) and private IP ranges
- Finding network address, broadcast address, first/last host, number of hosts

#### 3. Protocols & Diagnostic Tools
- TCP vs UDP (connection-oriented vs connectionless)
- Three-way handshake (SYN, SYN-ACK, ACK) and four-way close
- HTTP/HTTPS, DNS, DHCP (DORA), FTP/SFTP, SSH, ICMP (ping, traceroute)

#### 4. Network Devices
- Hub (Layer 1), Switch (Layer 2), Router (Layer 3), Firewall, Default Gateway, ARP, NAT

---

## 🛠 Features

### `index.html` — Dashboard
- **Cram / Normal mode toggle** (persisted in localStorage)
- **Definitions Matcher** — 8 randomized pairs, shake on wrong, glow on correct
- **OSI Model Quick Reference** — 7 layers with interactive protocol tags
- **Step-by-Step Solvers** (Normal mode only):
  - Tab 1: CPU Scheduling Simulator — FCFS, SJF, Round Robin with Gantt chart and waiting times
  - Tab 2: Subnetting Calculator — Network, broadcast, usable IP range, host count
  - Tab 3: Page Replacement Simulator — FIFO, LRU page fault calculations
  - Tab 4: IP Converter — Dotted decimal to binary and back
  - Tab 5: Linux Command Reference — Searchable CLI command library
  - Tab 6: IoT, VLAN & Licenses — Interactive VLAN frame tagging, software license compliance, wireless reference

### `smart_cram_cards.html` — Flashcards
- **67 high-yield cards** across 5 categories
- **3D perspective flip animation** (CSS preserve-3d)
- **Deck selector tabs:** All · OS Concepts · Memory · Networking · Protocols · Linux
- **Know it / Review rating** with localStorage persistence
- **Weak card checklist** — visual review list
- **Keyboard shortcuts:** Space=flip, ←→=navigate, 1=review, 2=know it
- **Stats row:** Total / Known / Review counts
- **Progress bar** tracking mastery

---

## ⌨ Keyboard Shortcuts (Flashcards)

| Key | Action |
|-----|--------|
| `Space` | Flip card |
| `←` | Previous card |
| `→` | Next card |
| `1` | Mark "Still Learning" |
| `2` | Mark "Know It!" |
| `R` | Shuffle deck |

---

## 🎨 Design

- **Background:** `#060810` deep dark space
- **Accent:** `#22d3ee` cyan + `#f97316` orange
- **Fonts:** Outfit (UI) + JetBrains Mono (code/diagnostics)
- Animated mesh gradient background
- Glassmorphic cards with backdrop-filter blur
- Hover lift effects + glow shadows
- Dark mode only — optimized for late-night study sessions

---

*Built for CZU Prague Operating Systems & Networks ETE2AE — exam focused, mobile ready, no internet required after loading fonts.*
