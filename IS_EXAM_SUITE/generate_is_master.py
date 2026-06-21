# -*- coding: utf-8 -*-
import os
import json

# 50 hand-crafted exam-accurate multiple-choice questions corresponding to the 50 cards
DATABASE = [
  {
    "q": "What are the four primary characteristics of a Data Warehouse, as summarized by the acronym SINV?",
    "options": [
      "Subject-oriented, Integrated, Non-volatile, and Variant-time (historical tracking).",
      "Structured, Indexed, Network-distributed, and Virtualized.",
      "Synchronous, Isolated, Normal-form, and Volatile.",
      "Subnetted, In-memory, Node-balanced, and Vectorized."
    ],
    "answers": [
      "Subject-oriented, Integrated, Non-volatile, and Variant-time (historical tracking)."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "What does the characteristic 'Non-volatile' mean in the context of a Data Warehouse?",
    "options": [
      "Data is stable and permanent; historical records are not updated or overwritten constantly like in OLTP.",
      "Data is stored in high-speed volatile RAM memory to enable rapid BI analytics queries.",
      "Data is automatically deleted after 90 days to comply with database storage space limitations.",
      "Data format changes dynamically depending on the client querying it."
    ],
    "answers": [
      "Data is stable and permanent; historical records are not updated or overwritten constantly like in OLTP."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "What is the meaning of the 'Time-variant' characteristic in a Data Warehouse?",
    "options": [
      "Data is linked to time/history; the warehouse stores historical snapshots to track trends over time.",
      "Data updates dynamically every second based on real-time sensor streams.",
      "The system varies query execution speed depending on peak network hours.",
      "Data is non-persistent and expires after a specific session time limit."
    ],
    "answers": [
      "Data is linked to time/history; the warehouse stores historical snapshots to track trends over time."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "What is the main operational purpose of a Data Warehouse?",
    "options": [
      "To support strategic analysis and decision-making by managers (analytical use).",
      "To process high-speed daily business transactions and operational logs.",
      "To serve as a DNS caching repository for corporate web traffic.",
      "To manage local system user permissions and group policies."
    ],
    "answers": [
      "To support strategic analysis and decision-making by managers (analytical use)."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "Which type of system is primarily designed to handle daily operational transactions?",
    "options": [
      "Transaction Processing System (TPS) / OLTP.",
      "Decision Support System (DSS) / OLAP.",
      "Executive Support System (ESS).",
      "Competitive Intelligence System (CIS)."
    ],
    "answers": [
      "Transaction Processing System (TPS) / OLTP."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "Which type of system is designed for strategic analysis and decision support?",
    "options": [
      "Data Warehouse / OLAP.",
      "Transaction Processing System (TPS) / OLTP.",
      "Domain Name System (DNS).",
      "Procure-to-Pay (P2P) billing interface."
    ],
    "answers": [
      "Data Warehouse / OLAP."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "What is the key difference between OLTP and OLAP systems?",
    "options": [
      "OLTP (Online Transaction Processing) handles daily operations/TPS; OLAP (Online Analytical Processing) handles strategic analysis/DW.",
      "OLTP manages analytical queries in a warehouse; OLAP handles operational transactions.",
      "OLTP stands for Object Linkage; OLAP stands for Operation Logic.",
      "OLTP runs only in the cloud; OLAP runs strictly on local, on-premise mainframes."
    ],
    "answers": [
      "OLTP (Online Transaction Processing) handles daily operations/TPS; OLAP (Online Analytical Processing) handles strategic analysis/DW."
    ],
    "cat": "Data Warehousing & BI"
  },
  {
    "q": "What does the abbreviation ERP stand for?",
    "options": [
      "Enterprise Resource Planning.",
      "Entity Relationship Protocol.",
      "Encrypted Routing Port.",
      "Electronic Resource Processing."
    ],
    "answers": [
      "Enterprise Resource Planning."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What does the abbreviation ERPS stand for?",
    "options": [
      "Enterprise Resource Planning System.",
      "Entity Relationship Pattern Standard.",
      "Enhanced Resource Port Server.",
      "External Routing Protocol Suite."
    ],
    "answers": [
      "Enterprise Resource Planning System."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "How do Information Systems (IS) and Enterprise Resource Planning (ERP) systems relate generally?",
    "options": [
      "IS is more general than ERP; an ERP is a specific type of Information System.",
      "ERP is more general than IS; an IS is a subset of an ERP system.",
      "They are completely unrelated; ERP refers only to hardware, and IS refers only to software.",
      "They are identical terms and can be used interchangeably in all contexts."
    ],
    "answers": [
      "IS is more general than ERP; an ERP is a specific type of Information System."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What is the main goal of an Enterprise Resource Planning (ERP) system in a corporation?",
    "options": [
      "To support the decision-making process by centralizing and standardizing business data across all departments.",
      "To replace human managers with automated software decision logic.",
      "To manage hardware CPU cycles and disk block allocations.",
      "To route network packets between corporate subnets and gateways."
    ],
    "answers": [
      "To support the decision-making process by centralizing and standardizing business data across all departments."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What is a major advantage of implementing an ERP system in an organization?",
    "options": [
      "Centralized data and visibility, which eliminates data silos and integrates workflows.",
      "Extremely low implementation and operational software costs.",
      "Eliminating the need for employee training or system administrators.",
      "Ensuring that the company is completely independent of software vendors."
    ],
    "answers": [
      "Centralized data and visibility, which eliminates data silos and integrates workflows."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What is a key disadvantage of deploying an Enterprise Resource Planning (ERP) system?",
    "options": [
      "High purchase/implementation costs and vendor lock-in.",
      "A complete lack of security updates or user access control features.",
      "Its inability to support financial modules or payroll reporting.",
      "It requires on-premise hardware and cannot run in a cloud model."
    ],
    "answers": [
      "High purchase/implementation costs and vendor lock-in."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What does the term 'vendor lock-in' mean in enterprise software?",
    "options": [
      "A company becomes highly dependent on one specific vendor, making switching software extremely difficult or costly.",
      "A software vendor locks user accounts when monthly subscription payments fail.",
      "The practice of locking physical server rooms to prevent unauthorized hardware access.",
      "A licensing model where software is free but cannot be updated."
    ],
    "answers": [
      "A company becomes highly dependent on one specific vendor, making switching software extremely difficult or costly."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "Which three companies represent the dominant leading vendors in the ERP/ERPS market?",
    "options": [
      "SAP, Oracle, and Microsoft.",
      "IBM, AWS, and Google.",
      "Apple, Meta, and Salesforce.",
      "RedHat, Cisco, and VMware."
    ],
    "answers": [
      "SAP, Oracle, and Microsoft."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What is SAP HANA, and what technology sets it apart?",
    "options": [
      "SAP's next-generation ERP platform that uses an in-memory database to process data in fast RAM.",
      "SAP's open-source operating system designed specifically for mobile smartphones.",
      "A hypervisor used to run multiple virtual machines on mainframes.",
      "A messaging queue protocol used to connect IoT client devices."
    ],
    "answers": [
      "SAP's next-generation ERP platform that uses an in-memory database to process data in fast RAM."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What is the primary operational advantage of an 'in-memory database'?",
    "options": [
      "Data is processed in high-speed RAM instead of on disk, enabling extremely fast analytics.",
      "Data is non-volatile and never requires a backup utility.",
      "It eliminates the need for database tables, keys, or schemas.",
      "It runs without consuming server electricity or CPU clock cycles."
    ],
    "answers": [
      "Data is processed in high-speed RAM instead of on disk, enabling extremely fast analytics."
    ],
    "cat": "Enterprise Resource Planning"
  },
  {
    "q": "What does the abbreviation DSS stand for?",
    "options": [
      "Decision Support System.",
      "Data Storage Structure.",
      "Distributed Security Server.",
      "Domain Subnet Solver."
    ],
    "answers": [
      "Decision Support System."
    ],
    "cat": "DSS"
  },
  {
    "q": "What is the definition and core purpose of a Decision Support System (DSS)?",
    "options": [
      "An interactive computer-based system that assists managers in decision-making by turning raw data into information.",
      "An automated compiler that turns high-level code into machine instructions.",
      "A routing protocol that selects the shortest path for network packets.",
      "An antivirus system that blocks malware from execution."
    ],
    "answers": [
      "An interactive computer-based system that assists managers in decision-making by turning raw data into information."
    ],
    "cat": "DSS"
  },
  {
    "q": "What transformation does a DSS perform to aid business managers?",
    "options": [
      "Transforms raw data into useful information.",
      "Transforms binary code into assembly language.",
      "Transforms local host names into IP addresses.",
      "Transforms relational schemas into flat CSV text."
    ],
    "answers": [
      "Transforms raw data into useful information."
    ],
    "cat": "DSS"
  },
  {
    "q": "What level of business decisions are Decision Support Systems (DSS) designed to assist?",
    "options": [
      "Strategic and tactical decisions.",
      "Routine daily operational transactions.",
      "Automatic hardware interrupt allocations.",
      "Physical storage defragmentation steps."
    ],
    "answers": [
      "Strategic and tactical decisions."
    ],
    "cat": "DSS"
  },
  {
    "q": "What is the role of a DSS relative to human managers?",
    "options": [
      "It is designed to support managers, not to replace them; human judgment remains essential.",
      "It is designed to replace human managers entirely with rule-based automated algorithms.",
      "It acts as a supervisor, monitoring manager performance and correcting mistakes.",
      "It serves only as a text editor for documentation templates."
    ],
    "answers": [
      "It is designed to support managers, not to replace them; human judgment remains essential."
    ],
    "cat": "DSS"
  },
  {
    "q": "What is a 'structured' decision?",
    "options": [
      "A decision where the entire procedure/solution can be specified in advance (e.g., calculating payroll).",
      "A decision that requires complete human intuition and cannot be programmed.",
      "A decision made exclusively by C-level executives in emergency board meetings.",
      "A decision where data inputs are missing or corrupt."
    ],
    "answers": [
      "A decision where the entire procedure/solution can be specified in advance (e.g., calculating payroll)."
    ],
    "cat": "DSS"
  },
  {
    "q": "What is an 'unstructured' decision?",
    "options": [
      "A decision where the procedure cannot be specified in advance, requiring human judgment and evaluation.",
      "A decision that can be completely automated by a simple database script.",
      "A decision that has no financial impact on the business operations.",
      "A decision involving only local network port configurations."
    ],
    "answers": [
      "A decision where the procedure cannot be specified in advance, requiring human judgment and evaluation."
    ],
    "cat": "DSS"
  },
  {
    "q": "What characterizes a 'semi-structured' decision?",
    "options": [
      "Some procedures can be specified, but human judgment is still required to make a final choice.",
      "It is calculated automatically by a computer, but must be signed on paper by a manager.",
      "It is unstructured on weekdays and structured on weekends.",
      "It uses exactly half the data inputs of a normal decision."
    ],
    "answers": [
      "Some procedures can be specified, but human judgment is still required to make a final choice."
    ],
    "cat": "DSS"
  },
  {
    "q": "In decision-making, what are the relative strengths of computers compared to humans?",
    "options": [
      "Computers process massive data quickly and consistently; humans excel at qualitative judgment and intuition.",
      "Computers possess superior creative intuition; humans excel at calculating massive floating-point operations.",
      "Computers handle emotional context; humans handle strict logical execution without error.",
      "There are no differences; computers and humans process decisions in the exact same manner."
    ],
    "answers": [
      "Computers process massive data quickly and consistently; humans excel at qualitative judgment and intuition."
    ],
    "cat": "DSS"
  },
  {
    "q": "What does the abbreviation BI stand for, and what does it do?",
    "options": [
      "Business Intelligence; helps companies analyze historical data and generate actionable insights.",
      "Binary Integration; compiles multi-source binaries into executable programs.",
      "Batch Interaction; executes scheduled scripts without user input.",
      "Broker Interface; connects publish-subscribe message queues."
    ],
    "answers": [
      "Business Intelligence; helps companies analyze historical data and generate actionable insights."
    ],
    "cat": "BI"
  },
  {
    "q": "What is Business Performance Management (BPM) and its general formula?",
    "options": [
      "BPM = BI + Planning; uses KPIs to monitor, align, and improve organizational performance.",
      "BPM = Databases + Operating Systems; runs local server processes.",
      "BPM = Cloud Services + APIs; integrates remote SaaS platforms.",
      "BPM = Security + Encryption; guards databases from unauthorized access."
    ],
    "answers": [
      "BPM = BI + Planning; uses KPIs to monitor, align, and improve organizational performance."
    ],
    "cat": "BI"
  },
  {
    "q": "What does the abbreviation KPI stand for?",
    "options": [
      "Key Performance Indicator.",
      "Kernel Process Interrupt.",
      "Keyboard Programming Interface.",
      "K-means Partition Index."
    ],
    "answers": [
      "Key Performance Indicator."
    ],
    "cat": "BI"
  },
  {
    "q": "What is the primary function of a Business Intelligence (BI) Dashboard?",
    "options": [
      "To visualize critical business metrics and KPIs in real-time for decision-makers.",
      "To allow developers to write database schemas and custom scripts.",
      "To configure network port forwarding and gateway security controls.",
      "To execute batch compilations of company software builds."
    ],
    "answers": [
      "To visualize critical business metrics and KPIs in real-time for decision-makers."
    ],
    "cat": "BI"
  },
  {
    "q": "What are the four core areas of Artificial Intelligence (AI) frequently tested on the exam?",
    "options": [
      "Natural Language Processing (NLP), Machine Learning, Computer Vision, and Deep Learning.",
      "Subnetting, Routing, DNS Resolution, and Port Forwarding.",
      "Gantt Scheduling, Page Replacement, Swapping, and Deadlocks.",
      "SaaS, IaaS, PaaS, and On-Premises computing."
    ],
    "answers": [
      "Natural Language Processing (NLP), Machine Learning, Computer Vision, and Deep Learning."
    ],
    "cat": "AI"
  },
  {
    "q": "What is the definition of Machine Learning (ML)?",
    "options": [
      "Algorithms that learn patterns from data without being explicitly programmed for each specific task.",
      "A hardware processor that contains multi-core ALU modules.",
      "A database server that automates table indexing and query optimization.",
      "A system that translates assembly code into machine-executable binaries."
    ],
    "answers": [
      "Algorithms that learn patterns from data without being explicitly programmed for each specific task."
    ],
    "cat": "AI"
  },
  {
    "q": "What biological structure inspired the creation of Artificial Neural Networks?",
    "options": [
      "The human brain and its network of interconnected neurons.",
      "The vascular root structure of terrestrial plants.",
      "The compound visual system of predatory insects.",
      "The double-helix molecular structure of DNA replication."
    ],
    "answers": [
      "The human brain and its network of interconnected neurons."
    ],
    "cat": "AI"
  },
  {
    "q": "What is 'Deep Learning' directly associated with?",
    "options": [
      "Multi-layer artificial neural networks with many hidden layers.",
      "Searching databases using highly complex nested SQL queries.",
      "Offline batch processing on mainframe computing architectures.",
      "Analyzing evolutionary phyloP conservation scores."
    ],
    "answers": [
      "Multi-layer artificial neural networks with many hidden layers."
    ],
    "cat": "AI"
  },
  {
    "q": "What is the primary focus of the AI field known as 'Computer Vision'?",
    "options": [
      "Interpreting, analyzing, and understanding visual data (images and video).",
      "Optimizing computer screen resolution and refresh rates.",
      "Tracing path algorithms in 3D gaming graphics rendering.",
      "Verifying user identity via optical fingerprint scanners."
    ],
    "answers": [
      "Interpreting, analyzing, and understanding visual data (images and video)."
    ],
    "cat": "AI"
  },
  {
    "q": "What does NLP stand for in AI, and what is its goal?",
    "options": [
      "Natural Language Processing; enabling computers to process, understand, and generate human language.",
      "Network Link Protocol; managing data transfer speeds between local clients.",
      "Numeric Logic Programming; solving mathematical constraints using logic compilers.",
      "Node Location Profile; mapping virtual servers in a cloud environment."
    ],
    "answers": [
      "Natural Language Processing; enabling computers to process, understand, and generate human language."
    ],
    "cat": "AI"
  },
  {
    "q": "Which trends represent major contemporary phenomena in modern Information Systems?",
    "options": [
      "Cloud computing, virtualization, big data, artificial intelligence, and cybersecurity.",
      "Batch punch cards, coaxial cabling, and floppy disk storage arrays.",
      "Command Line Interfaces replacing graphical user interfaces globally.",
      "An increase in on-premises mainframe usage and proprietary analog systems."
    ],
    "answers": [
      "Cloud computing, virtualization, big data, artificial intelligence, and cybersecurity."
    ],
    "cat": "AI"
  },
  {
    "q": "What is 'Cloud Computing' and what is its core billing concept?",
    "options": [
      "Delivery of IT services via the internet using a scalable, on-demand 'pay-for-what-you-use' utility model.",
      "Running calculations on weather models using specialized meteorological satellites.",
      "Storing encrypted document files on physical local backup tape drives.",
      "A networking method that transmits data via high-altitude atmospheric relays."
    ],
    "answers": [
      "Delivery of IT services via the internet using a scalable, on-demand 'pay-for-what-you-use' utility model."
    ],
    "cat": "Cloud Computing Services"
  },
  {
    "q": "What is SaaS, and what is a typical enterprise example?",
    "options": [
      "Software as a Service; application delivered entirely over the internet (e.g., Gmail, Microsoft Office 365).",
      "System as a Service; physical server leasing model.",
      "Security as a Service; firewall and threat monitoring hardware installation.",
      "Storage as a Service; local hard drive partition hosting."
    ],
    "answers": [
      "Software as a Service; application delivered entirely over the internet (e.g., Gmail, Microsoft Office 365)."
    ],
    "cat": "Cloud Computing Services"
  },
  {
    "q": "What is IaaS, and what is a typical cloud example?",
    "options": [
      "Infrastructure as a Service; provides raw computing hardware, virtual machines, and storage (e.g., AWS EC2).",
      "Integration as a Service; resolves database schema conversion mappings.",
      "Information as a Service; sells consolidated customer marketing logs.",
      "Internet as a Service; provides fiber-optic broadband connectivity."
    ],
    "answers": [
      "Infrastructure as a Service; provides raw computing hardware, virtual machines, and storage (e.g., AWS EC2)."
    ],
    "cat": "Cloud Computing Services"
  },
  {
    "q": "What is PaaS, and how does it relate to developer deployment?",
    "options": [
      "Platform as a Service; provides an operating system and runtime execution environment for custom code deployment.",
      "Port as a Service; leases public IP addresses and DNS records.",
      "Process as a Service; automates employee hiring and onboarding steps.",
      "Protocol as a Service; manages TCP/UDP handshake rules."
    ],
    "answers": [
      "Platform as a Service; provides an operating system and runtime execution environment for custom code deployment."
    ],
    "cat": "Cloud Computing Services"
  },
  {
    "q": "What is the core billing concept/idea behind the cloud business model?",
    "options": [
      "Pay-for-what-you-use; operational expenditure instead of heavy capital investment.",
      "A fixed yearly contract regardless of server CPU or network usage levels.",
      "Paying licensing fees per CPU transistor in the cloud datacenters.",
      "Free hosting supported entirely by third-party advertising grids."
    ],
    "answers": [
      "Pay-for-what-you-use; operational expenditure instead of heavy capital investment."
    ],
    "cat": "Cloud Computing Services"
  },
  {
    "q": "How has enterprise application architecture evolved over time?",
    "options": [
      "Evolved toward loosely coupled, interoperable Service-Oriented Architectures (SOA) and APIs.",
      "Evolved toward heavy monolithic programs running on centralized standalone mainframes.",
      "Evolved toward purely peer-to-peer desktop applications that reject server infrastructure.",
      "Evolved toward local batch processing systems without network connections."
    ],
    "answers": [
      "Evolved toward loosely coupled, interoperable Service-Oriented Architectures (SOA) and APIs."
    ],
    "cat": "Cloud Computing Services"
  },
  {
    "q": "What is Competitive Intelligence (CI), and what is its strict legal boundary?",
    "options": [
      "Legal and ethical gathering of competitor information using public resources; never corporate espionage.",
      "Hacking into competitor database servers to copy confidential proprietary code.",
      "Posing as a vendor to steal physical product blueprints from a competitor's office.",
      "Bribing competitor employees to obtain secret financial statements."
    ],
    "answers": [
      "Legal and ethical gathering of competitor information using public resources; never corporate espionage."
    ],
    "cat": "CI"
  },
  {
    "q": "How does Competitive Intelligence (CI) support corporate leadership?",
    "options": [
      "By improving understanding of the competitive environment to aid strategic planning.",
      "By automating daily financial invoice entries in the ERP ledger.",
      "By generating patent lawsuits to block competing market entries.",
      "By verifying that local system administrators comply with ISO standards."
    ],
    "answers": [
      "By improving understanding of the competitive environment to aid strategic planning."
    ],
    "cat": "CI"
  },
  {
    "q": "What sources are acceptable for ethical Competitive Intelligence (CI) gathering?",
    "options": [
      "Public and legal sources only, such as press releases, news, public databases, and government reports.",
      "Intercepted emails, stolen data dumps, and phone wiretaps.",
      "Confidential customer records leaked by corrupt database administrators.",
      "Proprietary code obtained via reverse-engineering compiled binary files."
    ],
    "answers": [
      "Public and legal sources only, such as press releases, news, public databases, and government reports."
    ],
    "cat": "CI"
  },
  {
    "q": "How do Information Systems (IS) and business management interact generally?",
    "options": [
      "They interact dynamically; IS supports management activities, and managers define system rules and constraints.",
      "They are completely isolated; IS operates autonomously without management oversight.",
      "Management is a subset of IS and is governed automatically by server algorithms.",
      "Information Systems have rendered human management structures obsolete in modern companies."
    ],
    "answers": [
      "They interact dynamically; IS supports management activities, and managers define system rules and constraints."
    ],
    "cat": "IS_BASICS"
  },
  {
    "q": "Who defines the operational rules, parameters, and settings in an Information System?",
    "options": [
      "Humans / managers.",
      "The system itself through self-generating logic code.",
      "The cloud hardware hypervisor automatically.",
      "The internet registry authority (IANA)."
    ],
    "answers": [
      "Humans / managers."
    ],
    "cat": "IS_BASICS"
  },
  {
    "q": "What is the ultimate organizational goal of an Information System in business management?",
    "options": [
      "To support management decision-making, not to replace the human decision-makers.",
      "To automate the firing of underperforming staff members.",
      "To maximize CPU clock utilization rates across all local hardware.",
      "To replace board directors with neural network models."
    ],
    "answers": [
      "To support management decision-making, not to replace the human decision-makers."
    ],
    "cat": "IS_BASICS"
  },
  {
    "q": "Which of the following is a classic example of an automated, rule-based Information System tool?",
    "options": [
      "Automatic stock reordering triggered when inventory falls below a user-defined threshold.",
      "A CEO negotiating a merger with a competing software developer.",
      "Conducting a legal performance review of a regional department head.",
      "Gathering competitive intelligence from public news feeds."
    ],
    "answers": [
      "Automatic stock reordering triggered when inventory falls below a user-defined threshold."
    ],
    "cat": "IS_BASICS"
  }
]

# Write out the interactive HTML file
def generate_html():
    # Read the raw Anki TSV file if it exists, otherwise use empty string
    anki_tsv_content = ""
    anki_path = "d:/CZUU/IS_EXAM_SUITE/anki_decks/IS_Anki_Deck.txt"
    if os.path.exists(anki_path):
        with open(anki_path, 'r', encoding='utf-8') as f:
            anki_tsv_content = f.read()

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🚀 IS Master Exam Suite | ETEA7E CZU Prague</title>
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
      --bg: #030510;
      --surface: #0a0d1e;
      --surface-hover: #131936;
      --surface-glass: rgba(10, 13, 30, 0.75);
      
      --accent: #06b6d4;        /* Electric Cyan */
      --accent-rgb: 6, 182, 212;
      --accent-glow: rgba(6, 182, 212, 0.25);
      
      --accent2: #f59e0b;       /* Warm Amber */
      --accent2-rgb: 245, 158, 11;
      --accent2-glow: rgba(245, 158, 11, 0.25);
      
      --violet: #c084fc;        /* Light Violet */
      --violet-glow: rgba(192, 132, 252, 0.2);
      
      --yellow: #fbbf24;        /* Gold Yellow */
      --red: #f87171;           /* Coral Red */
      --green: #4ade80;         /* Emerald Green */
      
      --text: #eef0f8;          /* Light slate text */
      --text-muted: #8b90a8;    /* Muted label text */
      --border: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(255, 255, 255, 0.15);
      
      --font: 'Outfit', sans-serif;
      --mono: 'JetBrains Mono', monospace;
      
      --radius: 16px;
      --radius-sm: 10px;
      --shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
    }

    /* Ambient Background blobs */
    .bg-blobs {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: -2;
      pointer-events: none;
      overflow: hidden;
    }
    .blob {
      position: absolute;
      border-radius: 50%;
      filter: blur(140px);
      opacity: 0.15;
    }
    .blob-1 {
      top: -10%; left: 15%;
      width: 400px; height: 400px;
      background: var(--accent);
    }
    .blob-2 {
      bottom: 10%; right: 15%;
      width: 500px; height: 500px;
      background: var(--accent2);
    }
    .blob-3 {
      top: 40%; left: 50%; transform: translate(-50%, -50%);
      width: 350px; height: 350px;
      background: var(--violet);
    }

    /* Grid pattern overlay */
    body::before {
      content: '';
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background-image: radial-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      background-size: 24px 24px;
      z-index: -1;
      pointer-events: none;
    }

    /* ─── STICKY HEADER ──────────────────────────── */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(3, 5, 16, 0.8);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #fff;
    }

    .brand-logo {
      font-size: 1.5rem;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 900;
      letter-spacing: -0.05em;
    }

    .brand-title {
      font-weight: 800;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }

    .brand-title span {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--accent2);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: 6px;
      vertical-align: middle;
      background: rgba(245, 158, 11, 0.1);
    }

    nav {
      display: flex;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border);
      border-radius: 30px;
      padding: 4px;
      gap: 2px;
    }

    .nav-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 16px;
      border-radius: 20px;
      font-family: var(--font);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .nav-btn:hover {
      color: var(--text);
      background: rgba(255, 255, 255, 0.05);
    }

    .nav-btn.active {
      background: linear-gradient(135deg, var(--accent), #0891b2);
      color: #000;
      font-weight: 700;
      box-shadow: 0 4px 12px rgba(6, 182, 212, 0.3);
    }

    /* ─── MAIN LAYOUT ────────────────────────────── */
    main {
      max-width: 1200px;
      margin: 2rem auto 4rem;
      padding: 0 1.5rem;
    }

    .panel-view {
      display: none;
      animation: fadeIn 0.4s ease-out forwards;
    }

    .panel-view.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Glass Panels */
    .glass-panel {
      background: var(--surface-glass);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      margin-bottom: 2rem;
      position: relative;
      overflow: hidden;
    }

    .glass-panel::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
    }

    /* Typography & Utilities */
    h2 {
      font-size: 1.75rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .panel-subtitle {
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-bottom: 1.5rem;
    }

    /* Pink Active-Recall Blur */
    .blur-reveal {
      filter: blur(5px);
      background-color: rgba(236, 72, 153, 0.15);
      border-radius: 4px;
      padding: 0 4px;
      cursor: pointer;
      transition: filter 0.2s ease, background-color 0.2s ease;
      color: #f472b6;
      border-bottom: 1px dashed rgba(236, 72, 153, 0.4);
    }

    .blur-reveal:hover, .blur-reveal.revealed {
      filter: blur(0);
      background-color: transparent;
      color: inherit;
      border-bottom-color: transparent;
    }

    /* ─── 1. CHECKLIST VIEW ───────────────────────── */
    .stats-summary {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .stat-card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .stat-info h3 {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 0.05em;
      margin-bottom: 4px;
    }

    .stat-info .num {
      font-size: 1.75rem;
      font-weight: 800;
      line-height: 1.1;
    }

    .stat-donut {
      width: 60px;
      height: 60px;
      transform: rotate(-90deg);
    }

    .stat-donut circle {
      fill: none;
      stroke-width: 5;
    }

    .stat-donut .circle-bg {
      stroke: rgba(255, 255, 255, 0.05);
    }

    .stat-donut .circle-fill {
      stroke-linecap: round;
      transition: stroke-dasharray 0.3s ease;
    }

    /* Filters Bar */
    .filter-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.5rem;
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      padding: 0.75rem;
      border-radius: var(--radius-sm);
    }

    .search-input {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 14px;
      color: #fff;
      font-family: var(--font);
      font-size: 0.85rem;
      width: 100%;
      max-width: 300px;
      outline: none;
      transition: all 0.2s;
    }

    .search-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 10px rgba(6, 182, 212, 0.15);
    }

    .filter-pills {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 4px;
      max-width: 100%;
    }

    .filter-pill {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 30px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .filter-pill:hover {
      color: var(--text);
      background: rgba(255, 255, 255, 0.06);
    }

    .filter-pill.active {
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--accent);
      color: var(--accent);
    }

    /* Checklist Grid */
    .checklist-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .chk-item {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      overflow: hidden;
      transition: border-color 0.2s, background-color 0.2s;
    }

    .chk-item:hover {
      border-color: var(--border-hover);
      background: rgba(255, 255, 255, 0.03);
    }

    .chk-item.mastered {
      border-left: 3px solid var(--green);
    }

    .chk-item.review {
      border-left: 3px solid var(--yellow);
    }

    .chk-header {
      padding: 1rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      gap: 1rem;
    }

    .chk-left {
      display: flex;
      align-items: center;
      gap: 12px;
      flex: 1;
    }

    .chk-checkbox {
      width: 20px;
      height: 20px;
      border-radius: 5px;
      border: 2px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
      flex-shrink: 0;
      background: var(--surface);
    }

    .chk-checkbox:hover {
      border-color: var(--accent);
    }

    .chk-checkbox.checked {
      background: var(--green);
      border-color: var(--green);
      color: #000;
    }

    .chk-checkbox.checked::after {
      content: '✓';
      font-size: 0.8rem;
      font-weight: 900;
    }

    .chk-title-group {
      display: flex;
      flex-direction: column;
    }

    .chk-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
    }

    .chk-meta {
      display: flex;
      gap: 8px;
      margin-top: 4px;
      align-items: center;
    }

    .chk-badge {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }

    .badge-cat {
      background: rgba(192, 132, 252, 0.1);
      color: var(--violet);
      border: 1px solid rgba(192, 132, 252, 0.2);
    }

    .star-btn {
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.1rem;
      transition: color 0.2s;
      display: flex;
      align-items: center;
    }

    .star-btn:hover {
      color: var(--yellow);
    }

    .star-btn.active {
      color: var(--yellow);
    }

    .chk-right {
      display: flex;
      align-items: center;
      gap: 12px;
      color: var(--text-muted);
    }

    .chk-arrow {
      transition: transform 0.2s;
    }

    .chk-item.expanded .chk-arrow {
      transform: rotate(180deg);
    }

    .chk-body {
      display: none;
      padding: 0 1.25rem 1.25rem 3.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.03);
      background: rgba(0, 0, 0, 0.1);
    }

    .chk-item.expanded .chk-body {
      display: block;
    }

    .ans-box {
      font-size: 0.88rem;
      line-height: 1.6;
      color: #d1d5db;
    }

    .ans-box p {
      margin-bottom: 8px;
    }

    .ans-box p:last-child {
      margin-bottom: 0;
    }

    /* ─── 2. FLASHCARDS VIEW ─────────────────────── */
    .fc-container {
      max-width: 580px;
      margin: 1rem auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.5rem;
    }

    .fc-progress-wrapper {
      width: 100%;
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .fc-progress-bar {
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 3px;
      overflow: hidden;
      margin-top: 6px;
      border: 1px solid var(--border);
    }

    .fc-progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      width: 0%;
      transition: width 0.3s ease;
    }

    /* 3D Card Flip */
    .fc-card-3d {
      width: 100%;
      height: 320px;
      perspective: 1000px;
      cursor: pointer;
    }

    .fc-card-inner {
      width: 100%;
      height: 100%;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .fc-card-3d.flipped .fc-card-inner {
      transform: rotateY(180deg);
    }

    .fc-face {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border-radius: var(--radius);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }

    .fc-front {
      background: radial-gradient(circle at 10% 10%, #111836 0%, var(--surface) 100%);
      color: #fff;
    }

    .fc-back {
      background: radial-gradient(circle at 90% 90%, #0d1e2e 0%, #080f1f 100%);
      transform: rotateY(180deg);
      border-color: rgba(6, 182, 212, 0.2);
    }

    .fc-cat {
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--accent2);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      align-self: flex-start;
      border: 1px solid rgba(245, 158, 11, 0.25);
      background: rgba(245, 158, 11, 0.08);
      padding: 2px 8px;
      border-radius: 4px;
    }

    .fc-text {
      font-size: 1.2rem;
      font-weight: 700;
      text-align: center;
      margin: auto 0;
      line-height: 1.5;
    }

    .fc-face.fc-back .fc-text {
      font-size: 0.95rem;
      font-weight: 500;
      color: #e2e8f0;
      text-align: left;
      overflow-y: auto;
      max-height: 190px;
      padding-right: 4px;
    }

    .fc-hint {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-align: center;
      font-style: italic;
    }

    .fc-actions {
      display: flex;
      gap: 12px;
      width: 100%;
    }

    .fc-btn {
      flex: 1;
      background: var(--surface-hover);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 10px;
      border-radius: var(--radius-sm);
      font-family: var(--font);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .fc-btn:hover {
      background: var(--border-hover);
      transform: translateY(-2px);
    }

    .fc-btn.primary {
      background: linear-gradient(135deg, var(--accent), #0891b2);
      color: #000;
      border: none;
      box-shadow: 0 4px 15px rgba(6, 182, 212, 0.25);
    }

    .fc-btn.primary:hover {
      box-shadow: 0 6px 20px rgba(6, 182, 212, 0.4);
    }

    /* Rating panel displayed on the back of card */
    .rating-row {
      display: none;
      gap: 8px;
      width: 100%;
      animation: slideUp 0.2s ease-out;
    }

    @keyframes slideUp {
      from { transform: translateY(5px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .rate-btn {
      flex: 1;
      border: none;
      padding: 10px;
      border-radius: 8px;
      font-family: var(--font);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      color: #000;
    }

    .rate-easy { background: var(--green); box-shadow: 0 4px 12px rgba(74, 222, 128, 0.2); }
    .rate-easy:hover { background: #34d399; transform: scale(1.02); }
    .rate-review { background: var(--yellow); box-shadow: 0 4px 12px rgba(251, 191, 36, 0.2); }
    .rate-review:hover { background: #fbbf24; transform: scale(1.02); }

    /* Shortcuts notice */
    .fc-shortcuts {
      font-size: 0.72rem;
      color: var(--text-muted);
      text-align: center;
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 20px;
    }

    /* ─── 3. MEMORIZE (AUDIO) VIEW ───────────────── */
    .audio-panel {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }

    @media (max-width: 768px) {
      .audio-panel {
        grid-template-columns: 1fr;
      }
    }

    .audio-left {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .audio-row {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .audio-row label {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }

    .audio-selector {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
      color: #fff;
      font-family: var(--font);
      font-size: 0.9rem;
      outline: none;
      cursor: pointer;
      width: 100%;
    }

    .custom-player {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    /* TTS Narrator Playlist */
    .tts-playlist {
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      max-height: 250px;
      overflow-y: auto;
      padding: 6px;
    }

    .tts-track {
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.15s;
    }

    .tts-track:hover {
      background: rgba(255, 255, 255, 0.03);
    }

    .tts-track.active {
      background: rgba(6, 182, 212, 0.1);
      border-left: 3px solid var(--accent);
      font-weight: 700;
      color: #fff;
    }

    /* ─── 4. MOCK EXAM VIEW ──────────────────────── */
    .exam-start-panel {
      text-align: center;
      max-width: 500px;
      margin: 2rem auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.25rem;
    }

    .exam-instructions {
      text-align: left;
      font-size: 0.88rem;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      padding: 1.25rem;
      border-radius: var(--radius-sm);
      width: 100%;
    }

    .exam-instructions li {
      margin-bottom: 6px;
      margin-left: 1.25rem;
    }

    .quiz-layout {
      display: grid;
      grid-template-columns: 1fr 280px;
      gap: 2rem;
    }

    @media (max-width: 850px) {
      .quiz-layout {
        grid-template-columns: 1fr;
      }
      .quiz-sidebar {
        order: -1;
      }
    }

    .quiz-sidebar {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      align-self: flex-start;
    }

    .timer-display {
      font-size: 1.8rem;
      font-weight: 800;
      font-family: var(--mono);
      text-align: center;
      color: var(--accent2);
      background: rgba(245, 158, 11, 0.06);
      border: 1px dashed rgba(245, 158, 11, 0.3);
      padding: 8px;
      border-radius: var(--radius-sm);
    }

    .nav-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
    }

    .quiz-nav-dot {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      height: 38px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 700;
      font-family: var(--mono);
      cursor: pointer;
      transition: all 0.2s;
    }

    .quiz-nav-dot:hover {
      border-color: var(--accent);
      color: #fff;
    }

    .quiz-nav-dot.answered {
      background: rgba(6, 182, 212, 0.1);
      border-color: var(--accent);
      color: var(--accent);
    }

    .quiz-nav-dot.current {
      background: var(--accent);
      border-color: var(--accent);
      color: #000;
      box-shadow: 0 0 10px rgba(6, 182, 212, 0.3);
    }

    .q-container {
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }

    .q-text {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      color: #fff;
    }

    .q-opts {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .q-opt-label {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.2s;
    }

    .q-opt-label:hover {
      border-color: var(--border-hover);
      background: var(--surface-hover);
    }

    .q-opt-label.selected {
      border-color: var(--accent);
      background: rgba(6, 182, 212, 0.05);
      color: #fff;
    }

    .q-opt-label input {
      accent-color: var(--accent);
    }

    /* Diagnostics results page */
    .res-score-box {
      text-align: center;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      padding: 2rem;
      border-radius: var(--radius);
      margin-bottom: 2rem;
    }

    .res-score-num {
      font-size: 3rem;
      font-weight: 900;
      font-family: var(--mono);
      line-height: 1.1;
      margin: 8px 0;
    }

    .diag-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .diag-card {
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1rem;
    }

    .diag-label {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .diag-bar-outer {
      height: 8px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 4px;
      overflow: hidden;
      margin-top: 8px;
    }

    .diag-bar-inner {
      height: 100%;
      border-radius: 4px;
      width: 0%;
      transition: width 1s ease-out;
    }

    /* ─── 5. SANDBOXES VIEW ───────────────────────── */
    .sandbox-tabs {
      display: flex;
      border-bottom: 1px solid var(--border);
      margin-bottom: 2rem;
      overflow-x: auto;
      gap: 8px;
      padding-bottom: 4px;
    }

    .sb-tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 10px 18px;
      font-family: var(--font);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
      border-bottom: 2px solid transparent;
    }

    .sb-tab-btn:hover {
      color: var(--text);
    }

    .sb-tab-btn.active {
      color: var(--accent);
      border-bottom-color: var(--accent);
      font-weight: 700;
    }

    .sb-view {
      display: none;
    }

    .sb-view.active {
      display: block;
    }

    /* Classifier Grid styling */
    .is-classifier-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 1rem;
    }
    
    .sb-scen-btn {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 14px;
      border-radius: var(--radius-sm);
      text-align: left;
      font-family: var(--font);
      font-size: 0.85rem;
      cursor: pointer;
      transition: all 0.2s;
      line-height: 1.45;
    }
    
    .sb-scen-btn:hover {
      border-color: var(--accent);
      background: var(--surface-hover);
    }
    
    .sb-scen-btn.active {
      border-color: var(--accent);
      background: rgba(6, 182, 212, 0.12);
      box-shadow: 0 0 10px rgba(6, 182, 212, 0.15);
    }

    /* P2P Flowchart styling */
    .p2p-timeline {
      display: flex;
      flex-direction: column;
      gap: 8px;
      max-width: 650px;
      margin: 0 auto;
    }

    .p2p-node {
      border: 1px solid var(--border);
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.02);
      overflow: hidden;
      cursor: pointer;
      transition: all 0.2s;
    }

    .p2p-node:hover {
      border-color: var(--accent2);
      background: rgba(245, 158, 11, 0.03);
    }

    .p2p-node.open {
      border-color: var(--accent);
    }

    .p2p-node-header {
      padding: 12px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .p2p-title-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .p2p-idx {
      font-family: var(--mono);
      font-weight: 700;
      color: var(--accent);
      background: rgba(6, 182, 212, 0.1);
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      font-size: 0.78rem;
    }

    .p2p-tcode {
      font-family: var(--mono);
      font-size: 0.72rem;
      background: rgba(245, 158, 11, 0.12);
      color: var(--accent2);
      border: 1px solid rgba(245, 158, 11, 0.25);
      padding: 1px 6px;
      border-radius: 4px;
      font-weight: 700;
    }

    .p2p-content {
      display: none;
      padding: 12px 16px 16px 56px;
      background: rgba(0, 0, 0, 0.1);
      border-top: 1px solid rgba(255, 255, 255, 0.03);
      font-size: 0.85rem;
      line-height: 1.5;
      color: var(--text-muted);
    }

    .p2p-node.open .p2p-content {
      display: block;
    }

    /* SDLC Matcher Grid */
    .sdlc-layout {
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 2rem;
    }

    @media (max-width: 768px) {
      .sdlc-layout {
        grid-template-columns: 1fr;
      }
    }

    .sdlc-phases-col {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .sdlc-phase-selector {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 10px 14px;
      border-radius: 8px;
      cursor: pointer;
      text-align: left;
      font-family: var(--font);
      font-size: 0.82rem;
      font-weight: 700;
      transition: all 0.2s;
    }

    .sdlc-phase-selector:hover {
      border-color: var(--accent);
      color: #fff;
    }

    .sdlc-phase-selector.active {
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--accent);
      color: var(--accent);
    }

    .sdlc-activities-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 8px;
    }

    .activity-chip {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 12px 14px;
      font-size: 0.8rem;
      color: var(--text);
      cursor: pointer;
      transition: all 0.2s;
      line-height: 1.4;
    }

    .activity-chip:hover {
      background: var(--surface-hover);
      border-color: var(--border-hover);
    }

    .activity-chip.correct {
      background: rgba(74, 222, 128, 0.15);
      border-color: var(--green);
      color: var(--green);
      cursor: default;
    }

    .activity-chip.wrong {
      background: rgba(248, 113, 113, 0.15);
      border-color: var(--red);
      color: var(--red);
    }

    /* Cloud Responsibility Matrix styling */
    .cloud-stack {
      display: flex;
      flex-direction: column-reverse;
      gap: 4px;
      max-width: 480px;
      margin: 1.5rem auto;
    }

    .cloud-layer {
      padding: 10px;
      border-radius: 6px;
      font-family: var(--mono);
      font-size: 0.78rem;
      font-weight: 700;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.3s ease;
      border: 1px solid var(--border);
    }

    .cloud-layer.user {
      background: rgba(245, 158, 11, 0.12);
      border-color: var(--accent2);
      color: var(--accent2);
    }

    .cloud-layer.provider {
      background: rgba(6, 182, 212, 0.08);
      border-color: var(--accent);
      color: var(--accent);
    }

    /* SAP Hierarchy */
    .sap-node-box {
      border: 1px solid var(--border);
      border-radius: 8px;
      background: var(--surface);
      padding: 12px;
      margin-bottom: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .sap-node-box:hover {
      border-color: var(--accent);
      background: var(--surface-hover);
    }

    .sap-node-box.active {
      border-color: var(--accent);
      background: rgba(6, 182, 212, 0.1);
    }

    .sap-desc-panel {
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      min-height: 120px;
    }

    /* ─── 6. CRAM MATERIAL VIEW ──────────────────── */
    .cram-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }

    @media (max-width: 768px) {
      .cram-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Matcher card item */
    .match-grid-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }

    .match-card-item {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px 12px;
      font-size: 0.78rem;
      cursor: pointer;
      min-height: 60px;
      display: flex;
      align-items: center;
      transition: all 0.2s;
      line-height: 1.45;
    }

    .match-card-item:hover {
      border-color: var(--accent);
      background: var(--surface-hover);
    }

    .match-card-item.selected {
      background: rgba(6, 182, 212, 0.1);
      border-color: var(--accent);
    }

    .match-card-item.matched {
      background: rgba(74, 222, 128, 0.05);
      border-color: rgba(74, 222, 128, 0.3);
      color: var(--green);
      cursor: default;
    }

    .match-card-item.wrong {
      animation: shake 0.3s;
      background: rgba(248, 113, 113, 0.1);
      border-color: var(--red);
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      25% { transform: translateX(-4px); }
      75% { transform: translateX(4px); }
    }

    .cram-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.78rem;
      margin-top: 8px;
    }

    .cram-table th, .cram-table td {
      border: 1px solid var(--border);
      padding: 8px 10px;
      text-align: left;
    }

    .cram-table th {
      background: rgba(255, 255, 255, 0.03);
      font-weight: 700;
      color: #fff;
    }

    .copier-box {
      width: 100%;
      height: 150px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text-muted);
      font-family: var(--mono);
      font-size: 0.72rem;
      padding: 10px;
      outline: none;
      resize: none;
    }
  </style>
</head>
<body>

  <!-- Ambient Blobs -->
  <div class="bg-blobs">
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>
  </div>

  <!-- Sticky Header -->
  <header>
    <a href="#" class="brand">
      <span class="brand-logo">ETEA7E</span>
      <div class="brand-title">IS Exam Suite<span>2H BLITZ</span></div>
    </a>
    <nav>
      <button class="nav-btn active" onclick="switchView('checklist')">📋 Checklist</button>
      <button class="nav-btn" onclick="switchView('flashcards')">🃏 Flashcards</button>
      <button class="nav-btn" onclick="switchView('memorize')">🧠 Memorize</button>
      <button class="nav-btn" onclick="switchView('exam')">📝 Mock Exam</button>
      <button class="nav-btn" onclick="switchView('sandboxes')">⚙️ Sandboxes</button>
      <button class="nav-btn" onclick="switchView('cram')">📚 Cram</button>
    </nav>
  </header>

  <!-- Main Content Container -->
  <main>

    <!-- 📋 PANEL 1: CHECKLIST -->
    <div class="panel-view active" id="view-checklist">
      <div class="glass-panel">
        <h2>📋 Active-Recall Memorization Checklist</h2>
        <p class="panel-subtitle">Review the 50 key concepts of the Information Systems course. Hover/tap pink blurred areas to reveal exam answers.</p>
        
        <!-- Stats Summary -->
        <div class="stats-summary">
          <div class="stat-card">
            <div class="stat-info">
              <h3>Mastered Cards</h3>
              <div class="num" id="stat-mastered-q">0 / 50</div>
            </div>
            <svg class="stat-donut">
              <circle class="circle-bg" cx="30" cy="30" r="25"></circle>
              <circle class="circle-fill" id="donut-mastery" cx="30" cy="30" r="25" stroke="var(--green)" stroke-dasharray="157" stroke-dashoffset="157"></circle>
            </svg>
          </div>
          <div class="stat-card">
            <div class="stat-info">
              <h3>Stashed for Review</h3>
              <div class="num" id="stat-review-q">0 / 50</div>
            </div>
            <svg class="stat-donut">
              <circle class="circle-bg" cx="30" cy="30" r="25"></circle>
              <circle class="circle-fill" id="donut-review" cx="30" cy="30" r="25" stroke="var(--yellow)" stroke-dasharray="157" stroke-dashoffset="157"></circle>
            </svg>
          </div>
          <div class="stat-card">
            <div class="stat-info">
              <h3>Completion Rate</h3>
              <div class="num" id="stat-mastery-pct">0%</div>
            </div>
            <svg class="stat-donut">
              <circle class="circle-bg" cx="30" cy="30" r="25"></circle>
              <circle class="circle-fill" id="donut-completion" cx="30" cy="30" r="25" stroke="var(--accent)" stroke-dasharray="157" stroke-dashoffset="157"></circle>
            </svg>
          </div>
        </div>

        <!-- Filters -->
        <div class="filter-bar">
          <input type="text" class="search-input" id="checklist-search" placeholder="🔍 Search concepts or key facts..." oninput="renderChecklist()">
          <div class="filter-pills" id="checklist-category-filters">
            <!-- Populated dynamically -->
          </div>
          <button class="fc-btn" id="checklist-reveal-btn" onclick="toggleRevealAll()" style="min-width: 170px;">👁️ Reveal Answers</button>
        </div>

        <!-- Cards List -->
        <div class="checklist-list" id="checklist-items-container">
          <!-- Injected via script -->
        </div>

      </div>
    </div>

    <!-- 🃏 PANEL 2: FLASHCARDS -->
    <div class="panel-view" id="view-flashcards">
      <div class="glass-panel">
        <h2>🃏 Active-Recall Smart Flashcards</h2>
        <p class="panel-subtitle">Quiz yourself on the 50 key concepts. Easy/Medium/Hard ratings feed back into your checklist metrics.</p>
        
        <div class="fc-container">
          <div class="fc-progress-wrapper">
            <span id="fc-count-text">Card 1 of 50</span>
            <span id="fc-completion-text">0% Staged</span>
          </div>
          <div class="fc-progress-bar">
            <div class="fc-progress-fill" id="fc-progress-bar-fill"></div>
          </div>
          
          <div class="fc-card-3d" id="fc-card" onclick="flipCard()">
            <div class="fc-card-inner">
              <!-- Front Face -->
              <div class="fc-face fc-front">
                <span class="fc-cat" id="fc-card-category">Data Warehousing</span>
                <div class="fc-text" id="fc-card-question">What does SINV stand for in a Data Warehouse?</div>
                <div class="fc-hint">💡 Click or press SPACE to flip card</div>
              </div>
              <!-- Back Face -->
              <div class="fc-face fc-back">
                <span class="fc-cat" style="border-color:rgba(74,222,128,0.3); background:rgba(74,222,128,0.08); color:var(--green)">Answer Definition</span>
                <div class="fc-text" id="fc-card-answer">Answer here</div>
                <div class="fc-hint">How well did you know this?</div>
              </div>
            </div>
          </div>

          <!-- Normal Actions -->
          <div class="fc-actions" id="fc-normal-actions">
            <button class="fc-btn" onclick="prevCard()">◀ Previous</button>
            <button class="fc-btn primary" onclick="flipCard()">🔁 Flip Card</button>
            <button class="fc-btn" onclick="nextCard()">Next ▶</button>
          </div>

          <!-- Rating Actions (shown on back face) -->
          <div class="rating-row" id="fc-rating-actions">
            <button class="rate-btn rate-review" onclick="rateCard(false)">❌ Still Learning (1)</button>
            <button class="rate-btn rate-easy" onclick="rateCard(true)">✅ Know It! (2)</button>
          </div>

          <div class="fc-shortcuts">
            ⌨️ Keyboard Shortcuts: [Space] Flip &nbsp;|&nbsp; [← / →] Navigate &nbsp;|&nbsp; [1 / 2] Rate Card
          </div>
        </div>

      </div>
    </div>

    <!-- 🧠 PANEL 3: MEMORIZE -->
    <div class="panel-view" id="view-memorize">
      <div class="glass-panel">
        <h2>🧠 Audio Guide Narrator &amp; Screen Wake Lock</h2>
        <p class="panel-subtitle">Listen to natural study guides while reading, or activate the TTS narrator playlist with speed adjustments.</p>
        
        <div class="audio-panel">
          <div class="audio-left">
            <div class="glass-panel" style="background: rgba(255,255,255,0.01); border: 1px solid var(--border); padding: 1.25rem; margin-bottom: 0;">
              <h3>🎧 Pre-Recorded Audio Podcast</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 1rem;">Generated natural accent variations. Safe to play in the background on mobile lock-screens.</p>
              
              <div class="audio-row" style="margin-bottom: 1rem;">
                <label for="is-audio-voice">Voice Accent: </label>
                <select id="is-audio-voice" onchange="changeISAudioVoice()" class="audio-selector">
                  <option value="is_audio_guide_us_male.mp3" selected>🇺🇸 US Male (Steffan)</option>
                  <option value="is_audio_guide_us_female.mp3">🇺🇸 US Female (Jenny)</option>
                  <option value="is_audio_guide_uk_male.mp3">🇬🇧 UK Male (Ryan)</option>
                  <option value="is_audio_guide_uk_female.mp3">🇬🇧 UK Female (Sonia)</option>
                </select>
              </div>
              
              <div class="custom-player">
                <audio id="is-audio-player" controls preload="none" style="width: 100%; outline: none;">
                  <source id="is-audio-source" src="is_audio_guide_us_male.mp3" type="audio/mpeg">
                </audio>
                <a id="is-audio-download" href="is_audio_guide_us_male.mp3" download class="fc-btn primary" style="text-decoration: none; text-align: center; height: 38px; display: inline-flex; align-items: center; justify-content: center;">⬇️ Download MP3</a>
              </div>
            </div>
            
            <div class="glass-panel" style="background: rgba(255,255,255,0.01); border: 1px solid var(--border); padding: 1.25rem; margin-bottom: 0;">
              <h3>🎙️ Screen Wake Lock Control</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 10px;">Forces your browser screen to stay awake during long-play study sessions.</p>
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 12px; height: 12px; border-radius: 50%; background: var(--red);" id="wake-lock-indicator"></div>
                <span id="wake-lock-status" style="font-size: 0.8rem; font-weight: 700;">Wake Lock: Inactive</span>
              </div>
            </div>
          </div>
          
          <!-- TTS Playlist right -->
          <div class="audio-right">
            <div class="glass-panel" style="background: rgba(255,255,255,0.01); border: 1px solid var(--border); padding: 1.25rem; margin-bottom: 0; height: 100%; display: flex; flex-direction: column;">
              <h3>🗣️ Browser TTS Narrator</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 1rem;">Synthesizes speech in real-time. Highlights the text blocks sequentially.</p>
              
              <div style="display: flex; gap: 8px; margin-bottom: 1rem;">
                <button class="fc-btn primary" id="tts-play-btn" onclick="toggleTTSPlayback()" style="max-width: 130px;">▶️ Play TTS</button>
                <button class="fc-btn" onclick="stopTTSPlayback()">⏹️ Stop</button>
                
                <select id="tts-speed" onchange="changeTTSSpeed()" class="audio-selector" style="max-width: 100px; padding: 6px;">
                  <option value="0.8">0.8x</option>
                  <option value="1.0" selected>1.0x</option>
                  <option value="1.2">1.2x</option>
                  <option value="1.5">1.5x</option>
                  <option value="2.0">2.0x</option>
                </select>
              </div>
              
              <div class="tts-playlist" id="tts-playlist-container" style="flex: 1;">
                <!-- Generated by JS -->
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- 📝 PANEL 4: MOCK EXAM -->
    <div class="panel-view" id="view-exam">
      <div class="glass-panel">
        <h2>📝 Timed Mock Exam Simulator</h2>
        <p class="panel-subtitle">Test yourself under real exam settings. Pulls 30 random questions from the database with category diagnostics.</p>
        
        <!-- Start screen -->
        <div id="exam-start-screen" class="exam-start-panel">
          <div style="font-size: 3rem;">📝</div>
          <h3>Start Information Systems Mock Exam</h3>
          <div class="exam-instructions">
            <ul>
              <li><strong>Count</strong>: 30 random questions from a database of 50 concepts.</li>
              <li><strong>Duration</strong>: 30 minutes (automatic submission when expired).</li>
              <li><strong>Format</strong>: Multiple-choice. Check boxes indicate multi-select questions.</li>
              <li><strong>Passing criteria</strong>: Minimum 60% required to pass.</li>
            </ul>
          </div>
          <button class="fc-btn primary" onclick="startMockExam()" style="min-width: 200px; height: 44px; font-size: 1rem;">🚀 Start Exam Now</button>
        </div>

        <!-- Quiz screen -->
        <div id="exam-quiz-screen" class="quiz-layout" style="display: none;">
          <div class="quiz-main">
            <div class="q-container">
              <div class="q-text" id="quiz-question-text">Question loading...</div>
              <div class="q-opts" id="quiz-options-container">
                <!-- Options -->
              </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <button class="fc-btn" onclick="quizPrevQuestion()">◀ Prev Question</button>
              <button class="fc-btn primary" id="quiz-submit-btn" onclick="submitExam()" style="max-width: 150px; background: linear-gradient(135deg, var(--red), #ef4444); color: #fff; display: none;">🏁 Submit Exam</button>
              <button class="fc-btn" onclick="quizNextQuestion()">Next Question ▶</button>
            </div>
          </div>
          
          <div class="quiz-sidebar">
            <div class="diag-label" style="text-align: center;">Remaining Time</div>
            <div class="timer-display" id="quiz-timer">30:00</div>
            <div class="diag-label" style="text-align: center; border-top: 1px solid var(--border); padding-top: 10px; margin-top: 5px;">Question Map</div>
            <div class="nav-grid" id="quiz-nav-grid">
              <!-- Navigation dots -->
            </div>
          </div>
        </div>

        <!-- Results screen -->
        <div id="exam-results-screen" style="display: none;">
          <div class="res-score-box">
            <h3 id="res-pass-label" style="color: var(--green); font-size: 1.5rem;">🎉 PASSED MOCK EXAM</h3>
            <div class="res-score-num" id="res-score-value">85%</div>
            <p id="res-score-desc">You answered 26 of 30 questions correctly.</p>
            <button class="fc-btn primary" onclick="resetMockExam()" style="margin-top: 1rem; max-width: 220px; display: inline-flex;">↺ Attempt Another Exam</button>
          </div>
          
          <h3>📊 Category Diagnostics Strength</h3>
          <p class="panel-subtitle">Review your category breakdowns below to identify weak topics.</p>
          <div class="diag-grid" id="res-diagnostics-container">
            <!-- Diagnostics bars -->
          </div>
          
          <h3 style="margin-top: 2rem;">🔍 Answers Review &amp; Corrections</h3>
          <p class="panel-subtitle">Carefully read explanations for wrong answers to avoid traps.</p>
          <div class="checklist-list" id="res-review-container">
            <!-- Review items -->
          </div>
        </div>

      </div>
    </div>

    <!-- ⚙️ PANEL 5: SANDBOXES -->
    <div class="panel-view" id="view-sandboxes">
      <div class="glass-panel">
        <h2>⚙️ Interactive Study Sandboxes &amp; Simulations</h2>
        <p class="panel-subtitle">Visual tools mapping directly to core concepts from the Information Systems syllabus.</p>
        
        <div class="sandbox-tabs">
          <button class="sb-tab-btn active" onclick="switchSandboxTab('classifier')">🧠 IS Type Classifier</button>
          <button class="sb-tab-btn" onclick="switchSandboxTab('p2p')">🔄 P2P Process Flow</button>
          <button class="sb-tab-btn" onclick="switchSandboxTab('sdlc')">📐 SDLC Phase Matcher</button>
          <button class="sb-tab-btn" onclick="switchSandboxTab('cloud')">☁️ Cloud Responsibility Matrix</button>
          <button class="sb-tab-btn" onclick="switchSandboxTab('sap')">🔒 SAP Authorization Hierarchy</button>
        </div>

        <!-- SB Tab 1: Classifier -->
        <div class="sb-view active" id="sb-classifier">
          <h3>🧠 Business Scenario Classifier</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.25rem;">Select a corporate activity to determine which class of Information System (TPS, MIS, DSS, EIS/ESS) supports it.</p>
          
          <div class="is-classifier-grid">
            <button class="sb-scen-btn" onclick="classifyScenario(this, 'TPS', '🛒 A cashier scans items at a grocery store checkout. The inventory updates and total revenue registers instantly.', 'Transaction Processing System (TPS) / OLTP: Handles routine, structured, daily operations. Data must execute in real time.')">
              🛒 Checkout Item Scan
            </button>
            <button class="sb-scen-btn" onclick="classifyScenario(this, 'MIS', '📊 A sales director gets a monthly spreadsheet detailing aggregate revenue generated per product category.', 'Management Information System (MIS): Consolidates structured operational TPS outputs into reports for middle management.')">
              📊 Monthly Category Sales Report
            </button>
            <button class="sb-scen-btn" onclick="classifyScenario(this, 'DSS', '📈 An airline analyst tests pricing strategies under high, medium, or low fuel cost projections.', 'Decision Support System (DSS): Renders analytical models and simulation tools to support semi-structured tactical planning.')">
              📈 Flight Fuel What-if Simulation
            </button>
            <button class="sb-scen-btn" onclick="classifyScenario(this, 'EIS/ESS', '🏢 The CEO views a consolidated dashboard displaying current stock price, revenue trend, and competitor news.', 'Executive Information / Support System (EIS/ESS): Aggregates high-level key performance metrics for strategic C-level decisions.')">
              🏢 Real-Time Global KPI Dashboard
            </button>
            <button class="sb-scen-btn" onclick="classifyScenario(this, 'TPS', '🏦 An account database checks balances and deducts cash immediately when a client withdraws from an ATM.', 'Transaction Processing System (TPS) / OLTP: Manages highly structured daily customer transactions (ATM cash withdrawal).')">
              🏦 ATM Cash Withdrawal
            </button>
            <button class="sb-scen-btn" onclick="classifyScenario(this, 'DSS', '💡 A warehouse manager runs scheduling models to determine which shift patterns minimize wage expenses.', 'Decision Support System (DSS): Uses numeric resource allocation models to solve semi-structured staffing questions.')">
              💡 Staffing Optimization Solver
            </button>
          </div>
          
          <div id="classifier-results-box" style="display: none; background: rgba(255,255,255,0.02); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; margin-top: 1.5rem;">
            <div style="font-size: 0.72rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 0.05em;">Classified System Type</div>
            <div id="classifier-res-type" style="font-size: 1.5rem; font-weight: 900; margin: 4px 0;">DSS</div>
            <div id="classifier-res-desc" style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5;">Description here.</div>
          </div>
        </div>

        <!-- SB Tab 2: P2P Flowchart -->
        <div class="sb-view" id="sb-p2p">
          <h3>🔄 Procure-to-Pay (P2P) SAP Lifecycle</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;">Click on each lifecycle node to inspect the transactional flowchart, description, and corresponding SAP Transaction Codes.</p>
          
          <div class="p2p-timeline">
            <!-- Node 1 -->
            <div class="p2p-node" onclick="toggleP2PNode(this)">
              <div class="p2p-node-header">
                <div class="p2p-title-group">
                  <div class="p2p-idx">01</div>
                  <strong>Purchase Requisition (PR)</strong>
                </div>
                <span class="p2p-tcode">ME51N</span>
              </div>
              <div class="p2p-content">
                Internal document created by a department indicating a need for materials. It goes through internal budget approvals but does not commit any funds to outside suppliers.
              </div>
            </div>
            
            <div style="text-align: center; color: var(--accent); font-size: 1.1rem; line-height: 1;">↓</div>
            
            <!-- Node 2 -->
            <div class="p2p-node" onclick="toggleP2PNode(this)">
              <div class="p2p-node-header">
                <div class="p2p-title-group">
                  <div class="p2p-idx">02</div>
                  <strong>Purchase Order (PO)</strong>
                </div>
                <span class="p2p-tcode">ME21N</span>
              </div>
              <div class="p2p-content">
                A formal, legally-binding offer sent to a external vendor specifying description, quantities, pricing, and shipment dates. Legally binds the company upon vendor confirmation.
              </div>
            </div>
            
            <div style="text-align: center; color: var(--accent); font-size: 1.1rem; line-height: 1;">↓</div>
            
            <!-- Node 3 -->
            <div class="p2p-node" onclick="toggleP2PNode(this)">
              <div class="p2p-node-header">
                <div class="p2p-title-group">
                  <div class="p2p-idx">03</div>
                  <strong>Goods Receipt (GR)</strong>
                </div>
                <span class="p2p-tcode">MIGO</span>
              </div>
              <div class="p2p-content">
                Warehouse clerk records physical material delivery arrival. The system updates inventory quantities and stamps the delivery document. Matches against PO lines.
              </div>
            </div>
            
            <div style="text-align: center; color: var(--accent); font-size: 1.1rem; line-height: 1;">↓</div>
            
            <!-- Node 4 -->
            <div class="p2p-node" onclick="toggleP2PNode(this)">
              <div class="p2p-node-header">
                <div class="p2p-title-group">
                  <div class="p2p-idx">04</div>
                  <strong>Invoice Verification (IV)</strong>
                </div>
                <span class="p2p-tcode">MIRO</span>
              </div>
              <div class="p2p-content">
                Accounts payable matches vendor invoice against original PO parameters and Warehouse GR tags (the classic 3-way match). Resolves variance errors.
              </div>
            </div>
            
            <div style="text-align: center; color: var(--accent); font-size: 1.1rem; line-height: 1;">↓</div>
            
            <!-- Node 5 -->
            <div class="p2p-node" onclick="toggleP2PNode(this)">
              <div class="p2p-node-header">
                <div class="p2p-title-group">
                  <div class="p2p-idx">05</div>
                  <strong>Outgoing Payment</strong>
                </div>
                <span class="p2p-tcode">F-53</span>
              </div>
              <div class="p2p-content">
                Clearing payment via bank transfer or cheque to finalize vendor obligations, closing the open account liability ledger entries.
              </div>
            </div>
          </div>
        </div>

        <!-- SB Tab 3: SDLC Matcher -->
        <div class="sb-view" id="sb-sdlc">
          <h3>📐 Systems Development Life Cycle (SDLC) Phase Matcher</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;">Select an SDLC phase on the left, then click on the activities on the right that belong to that phase. Complete all to master the SDLC lifecycle.</p>
          
          <div class="sdlc-layout">
            <div class="sdlc-phases-col">
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Planning')">📅 1. Planning</button>
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Analysis')">🔍 2. Analysis</button>
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Design')">✏️ 3. Design</button>
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Development')">💻 4. Development</button>
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Testing')">🧪 5. Testing</button>
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Implementation')">🚀 6. Implementation</button>
              <button class="sdlc-phase-selector" onclick="selectSDLCPhase(this, 'Maintenance')">🔧 7. Maintenance</button>
            </div>
            
            <div>
              <div id="sdlc-hint-box" style="margin-bottom: 10px; font-size: 0.82rem; font-weight: 700; color: var(--accent2);">Select a phase button on the left to begin...</div>
              
              <div class="sdlc-activities-grid">
                <div class="activity-chip" data-phase="Planning" onclick="clickSDLCActivity(this)">Feasibility Study</div>
                <div class="activity-chip" data-phase="Planning" onclick="clickSDLCActivity(this)">Project Scope Definition</div>
                <div class="activity-chip" data-phase="Analysis" onclick="clickSDLCActivity(this)">Gathering User Requirements</div>
                <div class="activity-chip" data-phase="Analysis" onclick="clickSDLCActivity(this)">Analyzing Existing Systems</div>
                <div class="activity-chip" data-phase="Design" onclick="clickSDLCActivity(this)">Data Flow Diagrams (DFD)</div>
                <div class="activity-chip" data-phase="Design" onclick="clickSDLCActivity(this)">Database Schema Modeling</div>
                <div class="activity-chip" data-phase="Development" onclick="clickSDLCActivity(this)">Writing Source Code</div>
                <div class="activity-chip" data-phase="Development" onclick="clickSDLCActivity(this)">Database Table Creation</div>
                <div class="activity-chip" data-phase="Testing" onclick="clickSDLCActivity(this)">Unit &amp; Integration Tests</div>
                <div class="activity-chip" data-phase="Testing" onclick="clickSDLCActivity(this)">User Acceptance Testing (UAT)</div>
                <div class="activity-chip" data-phase="Implementation" onclick="clickSDLCActivity(this)">Data Migration &amp; Import</div>
                <div class="activity-chip" data-phase="Implementation" onclick="clickSDLCActivity(this)">Staff Training Sessions</div>
                <div class="activity-chip" data-phase="Maintenance" onclick="clickSDLCActivity(this)">Bug Fixing &amp; Patching</div>
                <div class="activity-chip" data-phase="Maintenance" onclick="clickSDLCActivity(this)">Help Desk Support</div>
              </div>
            </div>
          </div>
        </div>

        <!-- SB Tab 4: Cloud Matrix -->
        <div class="sb-view" id="sb-cloud">
          <h3>☁️ Cloud Computing Shared Responsibility Matrix</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;">Select the deployment models (On-Premise, IaaS, PaaS, SaaS) to see how the responsibilities are shared between you (Amber) and the Provider (Cyan).</p>
          
          <div style="display: flex; gap: 8px; justify-content: center; margin-bottom: 1.5rem;">
            <button class="filter-pill active" id="btn-cloud-prem" onclick="setCloudModel('prem')">🏢 On-Premises</button>
            <button class="filter-pill" id="btn-cloud-iaas" onclick="setCloudModel('iaas')">☁️ IaaS (Infrastructure)</button>
            <button class="filter-pill" id="btn-cloud-paas" onclick="setCloudModel('paas')">☁️ PaaS (Platform)</button>
            <button class="filter-pill" id="btn-cloud-saas" onclick="setCloudModel('saas')">☁️ SaaS (Software)</button>
          </div>
          
          <div class="cloud-stack" id="cloud-stack-container">
            <div class="cloud-layer" id="layer-networking"><span>Networking</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-storage"><span>Storage</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-servers"><span>Physical Servers</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-virt"><span>Virtualization</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-os"><span>Operating System</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-mid"><span>Middleware</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-run"><span>Runtime</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-data"><span>Data &amp; Databases</span><span class="l-status">Managed</span></div>
            <div class="cloud-layer" id="layer-app"><span>Applications</span><span class="l-status">Managed</span></div>
          </div>
        </div>

        <!-- SB Tab 5: SAP Authorization -->
        <div class="sb-view" id="sb-sap">
          <h3>🔒 SAP Authorization Role Hierarchy</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;">Click on each level of the hierarchy tree to understand how permissions inherit and resolve in SAP authorization profiles.</p>
          
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
            <div>
              <div class="sap-node-box active" onclick="showSAPNode(this, 'user')">
                👥 <strong>1. User Account (SU01)</strong>
              </div>
              <div style="text-align: center; color: var(--accent); font-size: 0.9rem; line-height: 1; margin-bottom: 4px;">↓</div>
              
              <div class="sap-node-box" onclick="showSAPNode(this, 'role')">
                ⚙️ <strong>2. Authorization Role (PFCG)</strong>
              </div>
              <div style="text-align: center; color: var(--accent); font-size: 0.9rem; line-height: 1; margin-bottom: 4px;">↓</div>
              
              <div class="sap-node-box" onclick="showSAPNode(this, 'profile')">
                📂 <strong>3. Authorization Profile</strong>
              </div>
              <div style="text-align: center; color: var(--accent); font-size: 0.9rem; line-height: 1; margin-bottom: 4px;">↓</div>
              
              <div class="sap-node-box" onclick="showSAPNode(this, 'object')">
                💎 <strong>4. Authorization Object</strong>
              </div>
              <div style="text-align: center; color: var(--accent); font-size: 0.9rem; line-height: 1; margin-bottom: 4px;">↓</div>
              
              <div class="sap-node-box" onclick="showSAPNode(this, 'field')">
                🔑 <strong>5. Authorization Field Values</strong>
              </div>
            </div>
            
            <div class="sap-desc-panel" id="sap-desc-box">
              <h4 id="sap-selected-title" style="color: var(--accent); margin-bottom: 8px;">1. User Account (SU01)</h4>
              <p id="sap-selected-text" style="font-size: 0.85rem; line-height: 1.5; color: var(--text-muted);">The final corporate entity assigned to an employee. Managed using SU01 transaction code. It has one or multiple Role assignments.</p>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- 📚 PANEL 6: CRAM MATERIAL -->
    <div class="panel-view" id="view-cram">
      <div class="glass-panel">
        <h2>📚 Cram Material &amp; Definitions Matcher</h2>
        <p class="panel-subtitle">Review summary cheat sheets, play the matching game, and copy the raw Anki TSV file directly.</p>
        
        <div class="cram-grid">
          
          <!-- Left: Definitions Matcher Game -->
          <div>
            <div class="glass-panel" style="background: rgba(255,255,255,0.01); border: 1px solid var(--border); padding: 1.25rem;">
              <h3>🎯 Interactive Matcher Game</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 1rem;">Match the key terms with their corresponding definitions. Matches turn green.</p>
              
              <div class="match-grid-layout" id="match-grid">
                <!-- Injected via JS -->
              </div>
              
              <div class="match-score" style="margin-top: 1rem;">
                <span id="mscore-text" style="font-weight: 700;">0 / 8 Matched</span>
                <div class="score-bar-wrap" style="flex: 1; height: 8px; background: rgba(255, 255, 255, 0.05); border-radius: 4px; overflow: hidden; margin: 0 10px;">
                  <div class="score-bar" id="mscore-bar" style="width: 0%; height: 100%; background: var(--green);"></div>
                </div>
                <span id="mscore-pct" style="font-weight: 700; color: var(--green);">0%</span>
              </div>
              <button class="fc-btn" onclick="initMatcher()" style="margin-top: 10px; max-width: 120px;">↺ Reset</button>
            </div>
            
            <div class="glass-panel" style="background: rgba(255,255,255,0.01); border: 1px solid var(--border); padding: 1.25rem; margin-top: 1.5rem;">
              <h3>⚠️ Exam Trap &amp; Pitfalls Warning</h3>
              <ul style="font-size: 0.82rem; line-height: 1.6; color: var(--text-muted); padding-left: 1rem; list-style-type: square;">
                <li><strong style="color: var(--red);">OLTP vs OLAP:</strong> OLTP = Operations, high transactions, structured (TPS). OLAP = Analytics, strategic, Data Warehouse. Do not mix their purposes!</li>
                <li><strong style="color: var(--red);">SAP Hana Database:</strong> Processed in RAM (in-memory), not local disk. Hana is a High-Performance Appliance.</li>
                <li><strong style="color: var(--red);">Authorization objects:</strong> PFCG manages Roles. SU01 manages Users.</li>
                <li><strong style="color: var(--red);">SaaS vs PaaS:</strong> SaaS provides ready applications (Gmail). PaaS provides environments for custom developer programs (Heroku).</li>
                <li><strong style="color: var(--red);">DSS:</strong> Supports semi-structured decisions, never replaces managers.</li>
              </ul>
            </div>
          </div>
          
          <!-- Right: Summary tables and Anki exporter -->
          <div>
            <div class="glass-panel" style="background: rgba(255,255,255,0.01); border: 1px solid var(--border); padding: 1.25rem; margin-bottom: 0;">
              <h3>📋 OLAP Operations summary</h3>
              <table class="cram-table">
                <thead>
                  <tr>
                    <th>Operation</th>
                    <th>Action</th>
                    <th>Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Slice</strong></td>
                    <td>Selects a single dimension layer</td>
                    <td>Show sales for '2026' only</td>
                  </tr>
                  <tr>
                    <td><strong>Dice</strong></td>
                    <td>Selects a sub-cube of dimensions</td>
                    <td>Sales of laptops in Europe in Q1</td>
                  </tr>
                  <tr>
                    <td><strong>Roll-Up</strong></td>
                    <td>Aggregates data up the hierarchy</td>
                    <td>Detail by cities → total country</td>
                  </tr>
                  <tr>
                    <td><strong>Drill-Down</strong></td>
                    <td>Breaks aggregate data down</td>
                    <td>Total country → detail by cities</td>
                  </tr>
                </tbody>
              </table>
              
              <h3 style="margin-top: 1.5rem;">📁 Anki TSV Exporter</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 10px;">Copy the TSV text below to import these 50 cards directly into your Anki deck desktop app.</p>
              <textarea class="copier-box" id="anki-tsv-copy-box" readonly onclick="this.select()"></textarea>
            </div>
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
      'Data Warehousing & BI': 'Data Warehouse',
      'Enterprise Resource Planning': 'ERP/SAP',
      'DSS': 'DSS/Decisions',
      'BI': 'Business Intel',
      'AI': 'AI/ML',
      'Cloud Computing Services': 'Cloud',
      'CI': 'Comp Intel',
      'IS_BASICS': 'IS Basics'
    }};

    // ════════════════════════════════════════════════════════════════
    // TIMERS & COUNTDOWN
    // ════════════════════════════════════════════════════════════════
    let countdownSecs = 1800; // 30 minutes
    let examTimerInterval = null;

    function updateCountdown() {{
      const el = document.getElementById('quiz-timer');
      if (!el) return;
      
      const m = Math.floor(countdownSecs / 60);
      const s = countdownSecs % 60;
      el.textContent = `${{String(m).padStart(2,'0')}}:${{String(s).padStart(2,'0')}}`;
      
      if (countdownSecs <= 0) {{
        clearInterval(examTimerInterval);
        submitExam(true);
      }} else {{
        countdownSecs--;
      }}
    }}

    // ════════════════════════════════════════════════════════════════
    // NAVIGATION TABS
    // ════════════════════════════════════════════════════════════════
    let ttsPlaying = false;
    function switchView(viewName) {{
      document.querySelectorAll('.panel-view').forEach(panel => panel.classList.remove('active'));
      document.querySelectorAll('header nav button').forEach(btn => btn.classList.remove('active'));
      
      const targetPanel = document.getElementById(`view-${{viewName}}`);
      if (targetPanel) targetPanel.classList.add('active');
      
      // Find corresponding button
      const navBtn = Array.from(document.querySelectorAll('header nav button')).find(b => b.textContent.toLowerCase().includes(viewName));
      if (navBtn) navBtn.classList.add('active');
      
      if (viewName !== 'memorize' && ttsPlaying) {{
        stopTTSPlayback();
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
        hash |= 0; // Convert to 32bit integer
      }}
      return 'q_' + Math.abs(hash);
    }}

    // ════════════════════════════════════════════════════════════════
    // LOCAL STORAGE PROGRESS SYSTEM
    // ════════════════════════════════════════════════════════════════
    function saveChecklistProgress() {{
      const mastered = [];
      const review = [];
      document.querySelectorAll('.chk-item').forEach(el => {{
        const hash = el.dataset.hash;
        if (el.classList.contains('mastered')) mastered.push(hash);
        if (el.classList.contains('review')) review.push(hash);
      }});
      localStorage.setItem('is_mastered_hashes', JSON.stringify(mastered));
      localStorage.setItem('is_review_hashes', JSON.stringify(review));
      updateOverallStats();
    }}

    function updateOverallStats() {{
      const masteredIds = JSON.parse(localStorage.getItem('is_mastered_hashes') || '[]');
      const reviewIds = JSON.parse(localStorage.getItem('is_review_hashes') || '[]');
      
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
      const completionPct = Math.round(((masteredCount + reviewCount) / (total * 2)) * 100) || 0;
      
      document.getElementById('stat-mastery-pct').textContent = `${{masteredPct}}%`;
      
      drawDonut('donut-mastery', masteredPct);
      drawDonut('donut-review', reviewPct);
      drawDonut('donut-completion', completionPct);
    }}

    function drawDonut(strokeId, pct) {{
      const circle = document.getElementById(strokeId);
      if (!circle) return;
      const radius = circle.r.baseVal.value;
      const circumference = 2 * Math.PI * radius;
      const offset = circumference - (pct / 100) * circumference;
      circle.style.strokeDasharray = `${{circumference}} ${{circumference}}`;
      circle.style.strokeDashoffset = offset;
    }}

    function toggleMasteryState(hash, state) {{
      const itemEl = document.querySelector(`.chk-item[data-hash="${{hash}}"]`);
      if (!itemEl) return;
      
      if (state === 'mastered') {{
        itemEl.classList.toggle('mastered');
        itemEl.classList.remove('review');
      }} else if (state === 'review') {{
        itemEl.classList.toggle('review');
        itemEl.classList.remove('mastered');
      }}
      saveChecklistProgress();
    }}

    // ════════════════════════════════════════════════════════════════
    // CHECKLIST RENDERER
    // ════════════════════════════════════════════════════════════════
    let activeCategoryFilter = 'all';

    function renderChecklist() {{
      const container = document.getElementById('checklist-items-container');
      const search = document.getElementById('checklist-search').value.toLowerCase();
      
      const masteredIds = JSON.parse(localStorage.getItem('is_mastered_hashes') || '[]');
      const reviewIds = JSON.parse(localStorage.getItem('is_review_hashes') || '[]');
      
      // Fetch categories for filters
      const categories = ['all', ...new Set(DATABASE.map(q => q.cat))];
      const filterWrap = document.getElementById('checklist-category-filters');
      if (filterWrap.innerHTML.trim() === '') {{
        filterWrap.innerHTML = categories.map(cat => {{
          const label = CAT_LABELS[cat] || cat;
          const activeClass = cat === activeCategoryFilter ? 'active' : '';
          return `<button class="filter-pill ${{activeClass}}" onclick="filterChecklistCategory('${{cat}}')">${{label}}</button>`;
        }}).join('');
      }}
      
      container.innerHTML = '';
      
      DATABASE.forEach(q => {{
        const hash = getQHash(q.q);
        const matchesSearch = q.q.toLowerCase().includes(search) || q.options.join(' ').toLowerCase().includes(search);
        const matchesCategory = activeCategoryFilter === 'all' || q.cat === activeCategoryFilter;
        
        if (!matchesSearch || !matchesCategory) return;
        
        const isMastered = masteredIds.includes(hash) ? 'mastered' : '';
        const isReview = reviewIds.includes(hash) ? 'review' : '';
        
        // Wrap words in answer to support active recall blur (look for words with specific symbols, or key words)
        let formattedAns = q.answers[0];
        // Format terms to support blur-reveal: wrap key bold segments
        formattedAns = formattedAns.replace(/<b>(.*?)<\/b>/g, '<span class="blur-reveal" onclick="event.stopPropagation(); this.classList.toggle(\'revealed\')">$1</span>');
        
        const itemHtml = `
          <div class="chk-item ${{isMastered}} ${{isReview}}" data-hash="${{hash}}">
            <div class="chk-header" onclick="toggleChecklistItem('${{hash}}')">
              <div class="chk-left">
                <div class="chk-checkbox ${{isMastered ? 'checked' : ''}}" onclick="event.stopPropagation(); toggleMasteryState('${{hash}}', 'mastered')"></div>
                <div class="chk-title-group">
                  <div class="chk-title">${{htmlEscape(q.q)}}</div>
                  <div class="chk-meta">
                    <span class="chk-badge badge-cat">${{CAT_LABELS[q.cat] || q.cat}}</span>
                  </div>
                </div>
              </div>
              <div class="chk-right">
                <div class="star-btn ${{isReview ? 'active' : ''}}" onclick="event.stopPropagation(); toggleMasteryState('${{hash}}', 'review')" title="Flag for Review">★</div>
                <div class="chk-arrow">▼</div>
              </div>
            </div>
            <div class="chk-body">
              <div class="ans-box">
                <p><strong>Answer:</strong> ${{formattedAns}}</p>
                <div style="margin-top: 10px; display:flex; gap: 8px;">
                  <button class="filter-pill" onclick="toggleMasteryState('${{hash}}', 'mastered')" style="padding:4px 10px; font-size:0.75rem; border-color:var(--green)">✓ Mastered</button>
                  <button class="filter-pill" onclick="toggleMasteryState('${{hash}}', 'review')" style="padding:4px 10px; font-size:0.75rem; border-color:var(--yellow)">★ Stash for Review</button>
                </div>
              </div>
            </div>
          </div>
        `;
        container.insertAdjacentHTML('beforeend', itemHtml);
      }});
    }}

    function toggleChecklistItem(hash) {{
      const itemEl = document.querySelector(`.chk-item[data-hash="${{hash}}"]`);
      if (itemEl) itemEl.classList.toggle('expanded');
    }}

    function filterChecklistCategory(cat) {{
      activeCategoryFilter = cat;
      document.querySelectorAll('#checklist-category-filters .filter-pill').forEach(btn => {{
        const label = btn.textContent;
        const matchedLabel = CAT_LABELS[cat] || cat;
        if (label === matchedLabel) btn.classList.add('active');
        else btn.classList.remove('active');
      }});
      // Rebuild filter buttons to ensure class stays correct
      const filterWrap = document.getElementById('checklist-category-filters');
      filterWrap.innerHTML = '';
      renderChecklist();
    }}

    // ════════════════════════════════════════════════════════════════
    // FLASHCARDS IMPLEMENTATION
    // ════════════════════════════════════════════════════════════════
    let currentFcIdx = 0;
    
    function initFlashcards() {{
      currentFcIdx = 0;
      showFcCard();
    }}

    function showFcCard() {{
      const card = DATABASE[currentFcIdx];
      const hash = getQHash(card.q);
      
      const categoryEl = document.getElementById('fc-card-category');
      const questionEl = document.getElementById('fc-card-question');
      const answerEl = document.getElementById('fc-card-answer');
      
      categoryEl.textContent = CAT_LABELS[card.cat] || card.cat;
      questionEl.textContent = card.q;
      answerEl.innerHTML = card.answers[0];
      
      // Update counters
      document.getElementById('fc-count-text').textContent = `Card ${{currentFcIdx + 1}} of ${{DATABASE.length}}`;
      const pct = Math.round(((currentFcIdx + 1) / DATABASE.length) * 100);
      document.getElementById('fc-completion-text').textContent = `${{pct}}% Staged`;
      document.getElementById('fc-progress-bar-fill').style.width = `${{pct}}%`;
      
      // Unflip card
      document.getElementById('fc-card').classList.remove('flipped');
      document.getElementById('fc-normal-actions').style.display = 'flex';
      document.getElementById('fc-rating-actions').style.display = 'none';
    }}

    function flipCard() {{
      const cardEl = document.getElementById('fc-card');
      cardEl.classList.toggle('flipped');
      
      const isFlipped = cardEl.classList.contains('flipped');
      document.getElementById('fc-normal-actions').style.display = isFlipped ? 'none' : 'flex';
      document.getElementById('fc-rating-actions').style.display = isFlipped ? 'flex' : 'none';
    }}

    function nextCard() {{
      if (currentFcIdx < DATABASE.length - 1) {{
        currentFcIdx++;
        showFcCard();
      }}
    }}

    function prevCard() {{
      if (currentFcIdx > 0) {{
        currentFcIdx--;
        showFcCard();
      }}
    }}

    function rateCard(known) {{
      const card = DATABASE[currentFcIdx];
      const hash = getQHash(card.q);
      
      if (known) {{
        toggleMasteryState(hash, 'mastered');
      }} else {{
        toggleMasteryState(hash, 'review');
      }}
      
      // Auto advance
      setTimeout(() => {{
        if (currentFcIdx < DATABASE.length - 1) {{
          nextCard();
        }} else {{
          alert('🎉 You have reached the end of the flashcard deck! Review your stats on the Checklist tab.');
        }}
      }}, 300);
    }}

    // Keyboard controls for Flashcards
    window.addEventListener('keydown', e => {{
      // Only process when in flashcard view
      const view = document.getElementById('view-flashcards');
      if (!view.classList.contains('active')) return;
      
      if (e.code === 'Space') {{
        e.preventDefault();
        flipCard();
      }} else if (e.code === 'ArrowLeft') {{
        prevCard();
      }} else if (e.code === 'ArrowRight') {{
        nextCard();
      }} else if (e.code === 'Digit1') {{
        // check if flipped to allow rating
        if (document.getElementById('fc-card').classList.contains('flipped')) {{
          rateCard(false);
        }}
      }} else if (e.code === 'Digit2') {{
        if (document.getElementById('fc-card').classList.contains('flipped')) {{
          rateCard(true);
        }}
      }}
    }});

    // ════════════════════════════════════════════════════════════════
    // MEMORIZE VIEW (AUDIO)
    // ════════════════════════════════════════════════════════════════
    function changeISAudioVoice() {{
      const select = document.getElementById('is-audio-voice');
      const player = document.getElementById('is-audio-player');
      const source = document.getElementById('is-audio-source');
      const download = document.getElementById('is-audio-download');
      
      const val = select.value;
      source.src = val;
      download.href = val;
      player.load();
    }}

    // Browser TTS Narrator implementation
    const TTS_TRACKS = [
      {{ title: "DW & SINV", text: "Track 1. Data Warehousing. A data warehouse has four characteristics, matching the acronym SINV. Subject-oriented, Integrated, Non-volatile, and Variant-time. It is designed to support analysis and strategic decision-making, not daily transactional operations." }},
      {{ title: "OLTP vs OLAP", text: "Track 2. OLTP versus OLAP. Transaction processing systems or OLTP handle daily transactions. Data warehouses or OLAP handle analytical processes. OLTP is for routine operations; OLAP is for strategic, historical analysis." }},
      {{ title: "ERP Main Goal", text: "Track 3. Enterprise Resource Planning. The main goal of an ERP system is to centralize and standardize business data across all corporate departments, supporting the decision-making process and eliminating data silos." }},
      {{ title: "SAP Hana In-Memory DB", text: "Track 4. SAP Hana. HANA is SAP's next-generation platform utilizing an in-memory database where calculations run directly in fast RAM rather than local disk storage. This results in real-time analytics." }},
      {{ title: "DSS Role & Decisions", text: "Track 5. Decision Support Systems. A DSS is an interactive computer-based tool designed to assist managers in resolving semi-structured decisions by turning raw data into information. It supports, but never replaces, managers." }},
      {{ title: "Structured vs Unstructured", text: "Track 6. Decision Types. A structured decision is fully programmed and repetitive, like payroll calculations. An unstructured decision cannot be specified in advance, relying on human judgment, intuition, and evaluation." }},
      {{ title: "AI Areas: NLP & ML", text: "Track 7. Artificial Intelligence. Key tested areas include Natural Language Processing for speech and text, Machine Learning for pattern identification, Computer Vision for images, and Deep Learning for multi-layer neural networks." }},
      {{ title: "Cloud Services: SaaS, PaaS, IaaS", text: "Track 8. Cloud models. Infrastructure as a Service provides virtual machines and storage. Platform as a Service provides operating systems and code runtimes. Software as a Service delivers completed applications." }},
      {{ title: "Competitive Intelligence", text: "Track 9. Competitive Intelligence. CI is the legal and ethical gathering of competitor information using public records. It never involves corporate espionage or database hacking." }},
      {{ title: "IS & Management Rules", text: "Track 10. Information System Rules. Information systems and management interact dynamically. Humans and managers set system parameters, and the system executes operational functions, like automatic stock reordering." }}
    ];

    let ttsCurrentTrackIdx = 0;
    let ttsUtterance = null;
    let ttsSpeed = 1.0;

    function buildTTSPlaylist() {{
      const container = document.getElementById('tts-playlist-container');
      container.innerHTML = '';
      TTS_TRACKS.forEach((track, idx) => {{
        const el = document.createElement('div');
        el.className = `tts-track ${{idx === ttsCurrentTrackIdx ? 'active' : ''}}`;
        el.innerHTML = `
          <span>${{track.title}}</span>
          <span style="font-size:0.7rem; color:var(--text-muted);">Track ${{idx+1}}</span>
        `;
        el.onclick = () => selectTTSTrack(idx);
        container.appendChild(el);
      }});
    }}

    function selectTTSTrack(idx) {{
      stopTTSPlayback();
      ttsCurrentTrackIdx = idx;
      buildTTSPlaylist();
      playTTSTrack();
    }}

    function playTTSTrack() {{
      if ('speechSynthesis' in window) {{
        const track = TTS_TRACKS[ttsCurrentTrackIdx];
        ttsUtterance = new SpeechSynthesisUtterance(track.text);
        ttsUtterance.rate = ttsSpeed;
        
        // Find a decent english voice
        const voices = window.speechSynthesis.getVoices();
        const englishVoice = voices.find(v => v.lang.startsWith('en')) || voices[0];
        if (englishVoice) ttsUtterance.voice = englishVoice;
        
        ttsUtterance.onend = () => {{
          // Auto advance playlist
          if (ttsCurrentTrackIdx < TTS_TRACKS.length - 1) {{
            selectTTSTrack(ttsCurrentTrackIdx + 1);
          }} else {{
            ttsPlaying = false;
            document.getElementById('tts-play-btn').textContent = '▶️ Play TTS';
            releaseWakeLock();
          }}
        }};
        
        ttsUtterance.onerror = () => {{
          ttsPlaying = false;
          document.getElementById('tts-play-btn').textContent = '▶️ Play TTS';
          releaseWakeLock();
        }};
        
        window.speechSynthesis.speak(ttsUtterance);
        ttsPlaying = true;
        document.getElementById('tts-play-btn').textContent = '⏸️ Pause';
        requestWakeLock();
      }} else {{
        alert('Browser TTS Speech Synthesis is not supported in this browser.');
      }}
    }}

    function toggleTTSPlayback() {{
      if (ttsPlaying) {{
        window.speechSynthesis.pause();
        ttsPlaying = false;
        document.getElementById('tts-play-btn').textContent = '▶️ Resume';
        releaseWakeLock();
      }} else {{
        if (window.speechSynthesis.paused) {{
          window.speechSynthesis.resume();
          ttsPlaying = true;
          document.getElementById('tts-play-btn').textContent = '⏸️ Pause';
          requestWakeLock();
        }} else {{
          playTTSTrack();
        }}
      }}
    }}

    function stopTTSPlayback() {{
      window.speechSynthesis.cancel();
      ttsPlaying = false;
      document.getElementById('tts-play-btn').textContent = '▶️ Play TTS';
      releaseWakeLock();
    }}

    function changeTTSSpeed() {{
      ttsSpeed = parseFloat(document.getElementById('tts-speed').value) || 1.0;
      if (ttsPlaying) {{
        stopTTSPlayback();
        playTTSTrack();
      }}
    }}

    // Ensure voices load
    function loadSystemVoices() {{
      if ('speechSynthesis' in window) {{
        window.speechSynthesis.getVoices();
      }}
    }}
    if ('speechSynthesis' in window) {{
      window.speechSynthesis.onvoiceschanged = loadSystemVoices;
    }}

    // ════════════════════════════════════════════════════════════════
    // WAKE LOCK API HOOKS
    // ════════════════════════════════════════════════════════════════
    let wakeLockObj = null;

    async function requestWakeLock() {{
      if ('wakeLock' in navigator) {{
        try {{
          wakeLockObj = await navigator.wakeLock.request('screen');
          updateWakeLockStatus(true);
          
          wakeLockObj.addEventListener('release', () => {{
            updateWakeLockStatus(false);
          }});
        }} catch (err) {{
          console.warn('Wake Lock request failed:', err.message);
        }}
      }}
    }}

    function releaseWakeLock() {{
      if (wakeLockObj != null) {{
        wakeLockObj.release();
        wakeLockObj = null;
        updateWakeLockStatus(false);
      }}
    }}

    function updateWakeLockStatus(active) {{
      const ind = document.getElementById('wake-lock-indicator');
      const txt = document.getElementById('wake-lock-status');
      if (ind & txt) {{
        ind.style.background = active ? 'var(--green)' : 'var(--red)';
        txt.textContent = active ? 'Wake Lock: Active' : 'Wake Lock: Inactive';
      }}
    }}

    // ════════════════════════════════════════════════════════════════
    // 4. MOCK EXAM TIMED SIMULATOR
    // ════════════════════════════════════════════════════════════════
    let quizSelectedQuestions = [];
    let quizCurrentIdx = 0;
    let quizAnswersMap = {{}}; // Map idx -> array of selected options

    function startMockExam() {{
      document.getElementById('exam-start-screen').style.display = 'none';
      document.getElementById('exam-quiz-screen').style.display = 'grid';
      document.getElementById('exam-results-screen').style.display = 'none';
      
      // Shuffle questions database and pick 30
      const pool = [...DATABASE];
      for (let i = pool.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [pool[i], pool[j]] = [pool[j], pool[i]];
      }}
      quizSelectedQuestions = pool.slice(0, 30);
      
      quizCurrentIdx = 0;
      quizAnswersMap = {{}};
      countdownSecs = 1800; // 30 minutes
      
      // Render question map grid dots
      const grid = document.getElementById('quiz-nav-grid');
      grid.innerHTML = '';
      for (let i = 0; i < 30; i++) {{
        const dot = document.createElement('div');
        dot.className = 'quiz-nav-dot';
        dot.textContent = i + 1;
        dot.onclick = () => loadQuizQuestion(i);
        grid.appendChild(dot);
      }}
      
      loadQuizQuestion(0);
      
      // Start Timer
      clearInterval(examTimerInterval);
      updateCountdown();
      examTimerInterval = setInterval(updateCountdown, 1000);
    }}

    function loadQuizQuestion(idx) {{
      quizCurrentIdx = idx;
      const question = quizSelectedQuestions[idx];
      
      // Highlight current dot
      document.querySelectorAll('#quiz-nav-grid .quiz-nav-dot').forEach((dot, dIdx) => {{
        dot.classList.remove('current');
        if (dIdx === idx) dot.classList.add('current');
      }});
      
      document.getElementById('quiz-question-text').textContent = `Question ${{idx+1}} of 30: ${{question.q}}`;
      
      const optWrap = document.getElementById('quiz-options-container');
      optWrap.innerHTML = '';
      
      // If answers length > 1, render checkboxes, else radio buttons
      const isMulti = question.answers.length > 1;
      
      question.options.forEach(opt => {{
        const isSel = (quizAnswersMap[idx] || []).includes(opt);
        const label = document.createElement('label');
        label.className = `q-opt-label ${{isSel ? 'selected' : ''}}`;
        
        const input = document.createElement('input');
        input.type = isMulti ? 'checkbox' : 'radio';
        input.name = 'quiz-option';
        input.checked = isSel;
        input.onclick = (e) => selectQuizOption(opt, isMulti);
        
        label.appendChild(input);
        label.appendChild(document.createTextNode(opt));
        optWrap.appendChild(label);
      }});
      
      // If last question, show submit button
      if (idx === 29) {{
        document.getElementById('quiz-submit-btn').style.display = 'block';
      }} else {{
        document.getElementById('quiz-submit-btn').style.display = 'none';
      }}
    }}

    function selectQuizOption(opt, isMulti) {{
      const idx = quizCurrentIdx;
      if (!quizAnswersMap[idx]) quizAnswersMap[idx] = [];
      
      if (isMulti) {{
        const optIdx = quizAnswersMap[idx].indexOf(opt);
        if (optIdx > -1) quizAnswersMap[idx].splice(optIdx, 1);
        else quizAnswersMap[idx].push(opt);
      }} else {{
        quizAnswersMap[idx] = [opt];
      }}
      
      // Mark navigation dot answered
      const dot = document.querySelectorAll('#quiz-nav-grid .quiz-nav-dot')[idx];
      if (quizAnswersMap[idx].length > 0) dot.classList.add('answered');
      else dot.classList.remove('answered');
      
      // Reload choices highlights
      loadQuizQuestion(idx);
    }}

    function quizNextQuestion() {{
      if (quizCurrentIdx < 29) loadQuizQuestion(quizCurrentIdx + 1);
    }}

    function quizPrevQuestion() {{
      if (quizCurrentIdx > 0) loadQuizQuestion(quizCurrentIdx - 1);
    }}

    function submitExam(expired = false) {{
      clearInterval(examTimerInterval);
      if (!expired) {{
        const confirmSub = confirm('Are you sure you want to submit your exam now?');
        if (!confirmSub) return;
      }}
      
      document.getElementById('exam-quiz-screen').style.display = 'none';
      document.getElementById('exam-results-screen').style.display = 'block';
      
      // Grade the exam
      let score = 0;
      let catScores = {{}}; // cat -> {{correct: 0, total: 0}}
      
      const reviewContainer = document.getElementById('res-review-container');
      reviewContainer.innerHTML = '';
      
      quizSelectedQuestions.forEach((q, idx) => {{
        const userAnswers = quizAnswersMap[idx] || [];
        const correctAnswers = q.answers;
        
        // Check if correct
        const matchesAllCorrect = correctAnswers.every(ans => userAnswers.includes(ans)) && userAnswers.length === correctAnswers.length;
        
        if (!catScores[q.cat]) catScores[q.cat] = {{ correct: 0, total: 0 }};
        catScores[q.cat].total++;
        
        if (matchesAllCorrect) {{
          score++;
          catScores[q.cat].correct++;
        }}
        
        // Append review card
        const hash = getQHash(q.q);
        const reviewHtml = `
          <div class="chk-item ${{matchesAllCorrect ? 'mastered' : 'review'}}">
            <div class="chk-header" onclick="toggleChecklistItem('${{hash}}_rev')">
              <div class="chk-left">
                <span style="font-size: 1.1rem;">${{matchesAllCorrect ? '✅' : '❌'}}</span>
                <div class="chk-title-group">
                  <div class="chk-title">${{htmlEscape(q.q)}}</div>
                  <div class="chk-meta">
                    <span class="chk-badge badge-cat">${{CAT_LABELS[q.cat] || q.cat}}</span>
                  </div>
                </div>
              </div>
              <div class="chk-right">
                <div class="chk-arrow">▼</div>
              </div>
            </div>
            <div class="chk-body" id="${{hash}}_rev_body" style="padding-left: 2.25rem;">
              <div class="ans-box">
                <p><strong>Your Selected Answer:</strong> ${{userAnswers.join('; ') || '<span style="color:var(--red);">No Answer Provided</span>'}}</p>
                <p><strong>Correct Answer:</strong> ${{correctAnswers.join('; ')}}</p>
                <p style="color: var(--text-muted); font-size:0.8rem; margin-top:8px;">💡 Remember to study this card in detail on the main Checklist panel.</p>
              </div>
            </div>
          </div>
        `;
        reviewContainer.insertAdjacentHTML('beforeend', reviewHtml);
      }});
      
      // Update score display
      const pct = Math.round((score / 30) * 100);
      const scoreValEl = document.getElementById('res-score-value');
      const scoreDescEl = document.getElementById('res-score-desc');
      const passLabelEl = document.getElementById('res-pass-label');
      
      scoreValEl.textContent = `${{pct}}%`;
      scoreDescEl.textContent = `You answered ${{score}} of 30 questions correctly.`;
      
      const passed = pct >= 60;
      passLabelEl.textContent = passed ? '🎉 PASSED MOCK EXAM' : '❌ FAILED MOCK EXAM (Passing score: 60%)';
      passLabelEl.style.color = passed ? 'var(--green)' : 'var(--red)';
      scoreValEl.style.color = passed ? 'var(--green)' : 'var(--red)';
      
      // Render Category diagnostics
      const diagContainer = document.getElementById('res-diagnostics-container');
      diagContainer.innerHTML = '';
      
      for (const [cat, data] of Object.entries(catScores)) {{
        const cPct = Math.round((data.correct / data.total) * 100) || 0;
        const color = cPct >= 75 ? 'var(--green)' : (cPct >= 60 ? 'var(--yellow)' : 'var(--red)');
        
        const cardHtml = `
          <div class="diag-card">
            <div class="diag-label">${{CAT_LABELS[cat] || cat}}</div>
            <div style="font-size: 1.25rem; font-weight: 800; margin-top:4px;">${{cPct}}%</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">${{data.correct}} of ${{data.total}} correct</div>
            <div class="diag-bar-outer">
              <div class="diag-bar-inner" style="width: ${{cPct}}%; background: ${{color}};"></div>
            </div>
          </div>
        `;
        diagContainer.insertAdjacentHTML('beforeend', cardHtml);
      }}
    }}

    function toggleChecklistItem(id) {{
      const header = event.currentTarget;
      const item = header.parentNode;
      item.classList.toggle('expanded');
      const body = item.querySelector('.chk-body');
      if (body) {{
        body.style.display = item.classList.contains('expanded') ? 'block' : 'none';
      }}
    }}

    function resetMockExam() {{
      document.getElementById('exam-start-screen').style.display = 'flex';
      document.getElementById('exam-quiz-screen').style.display = 'none';
      document.getElementById('exam-results-screen').style.display = 'none';
    }}

    // ════════════════════════════════════════════════════════════════
    // 5. STUDY SANDBOXES TABS
    // ════════════════════════════════════════════════════════════════
    function switchSandboxTab(tabName) {{
      document.querySelectorAll('.sb-tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.sb-view').forEach(view => view.classList.remove('active'));
      
      // Find matching tab button
      const btn = Array.from(document.querySelectorAll('.sb-tab-btn')).find(b => b.textContent.toLowerCase().includes(tabName));
      if (btn) btn.classList.add('active');
      
      const view = document.getElementById(`sb-${{tabName}}`);
      if (view) view.classList.add('active');
    }}

    // Sandbox 1: Scenario Classifier
    let lastActiveClassifierBtn = null;
    function classifyScenario(btn, type, scenText, explanation) {{
      if (lastActiveClassifierBtn) lastActiveClassifierBtn.classList.remove('active');
      btn.classList.add('active');
      lastActiveClassifierBtn = btn;
      
      document.getElementById('classifier-results-box').style.display = 'block';
      document.getElementById('classifier-res-type').textContent = type;
      document.getElementById('classifier-res-desc').textContent = explanation;
    }}

    // Sandbox 2: P2P Flowchart
    function toggleP2PNode(nodeEl) {{
      const isOpen = nodeEl.classList.contains('open');
      document.querySelectorAll('.p2p-node').forEach(n => n.classList.remove('open'));
      if (!isOpen) nodeEl.classList.add('open');
    }}

    // Sandbox 3: SDLC Phase Matcher
    let activeSDLCPhase = null;
    function selectSDLCPhase(btn, phase) {{
      activeSDLCPhase = phase;
      document.querySelectorAll('.sdlc-phase-selector').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      document.getElementById('sdlc-hint-box').textContent = `Target Phase: "${{phase}}" — Now click matching activities below.`;
      
      // Clear wrong stylings
      document.querySelectorAll('.activity-chip').forEach(c => {{
        if (!c.classList.contains('correct')) c.classList.remove('wrong');
      }});
    }}

    function clickSDLCActivity(chip) {{
      if (!activeSDLCPhase) {{
        alert('Please select an SDLC Phase on the left column first!');
        return;
      }}
      
      if (chip.classList.contains('correct')) return;
      
      const correctPhase = chip.dataset.phase;
      if (correctPhase === activeSDLCPhase) {{
        chip.classList.add('correct');
        document.getElementById('sdlc-hint-box').innerHTML = `✅ <strong>Correct!</strong> "${{chip.textContent}}" belongs to the ${{correctPhase}} phase.`;
        
        // Check if all correct
        const uncompleted = Array.from(document.querySelectorAll('.activity-chip')).filter(c => !c.classList.contains('correct'));
        if (uncompleted.length === 0) {{
          setTimeout(() => {{
            alert('🎉 Perfect! You mapped all SDLC activities to their correct phases.');
          }}, 300);
        }}
      }} else {{
        chip.classList.add('wrong');
        setTimeout(() => chip.classList.remove('wrong'), 400);
        document.getElementById('sdlc-hint-box').innerHTML = `❌ <strong>Wrong:</strong> "${{chip.textContent}}" belongs to the <span style="color:var(--accent); font-weight:700;">${{correctPhase}}</span> phase.`;
      }}
    }}

    // Sandbox 4: Cloud Matrix
    const cloudLayers = {{
      prem: ['networking', 'storage', 'servers', 'virt', 'os', 'mid', 'run', 'data', 'app'],
      iaas: ['networking', 'storage', 'servers', 'virt'],
      paas: ['networking', 'storage', 'servers', 'virt', 'os', 'mid', 'run'],
      saas: ['networking', 'storage', 'servers', 'virt', 'os', 'mid', 'run', 'data', 'app']
    }};

    function setCloudModel(model) {{
      document.querySelectorAll('.filter-pill').forEach(btn => {{
        if (btn.id === `btn-cloud-${{model}}`) btn.classList.add('active');
        else btn.classList.remove('active');
      }});
      
      const providerLayers = cloudLayers[model];
      
      // Update each layer status
      document.querySelectorAll('.cloud-layer').forEach(layer => {{
        const layerId = layer.id.replace('layer-', '');
        const isProvider = providerLayers.includes(layerId);
        
        layer.className = `cloud-layer ${{isProvider ? 'provider' : 'user'}}`;
        const statusSpan = layer.querySelector('.l-status');
        
        if (model === 'saas' && layerId === 'app') {{
          // SaaS has tiny customer configurations
          statusSpan.textContent = 'Vendor Managed (Shared)';
        }} else {{
          statusSpan.textContent = isProvider ? 'Cloud Provider Managed' : 'You Manage';
        }}
      }});
    }}

    // Sandbox 5: SAP Authorization
    const sapNodes = {{
      user: {{
        title: "1. User Account (SU01)",
        text: "The final corporate entity assigned to an employee. Managed using the SU01 transaction code in SAP. It serves as the login record and is assigned one or multiple Roles."
      }},
      role: {{
        title: "2. Authorization Role (PFCG)",
        text: "Logical grouping of business functions and transaction codes. Created and managed in the Profile Generator (PFCG). Roles generate Profiles."
      }},
      profile: {{
        title: "3. Authorization Profile",
        text: "The technical container compiled from roles, containing raw authorization objects. Profiles are what the system actually reads during authorization check gates."
      }},
      object: {{
        title: "4. Authorization Object",
        text: "The security gatekeeper in the ABAP code (e.g., S_TCODE or M_BEST_BSA). Contains up to 10 security fields checked simultaneously to prevent unauthorized actions."
      }},
      field: {{
        title: "5. Authorization Field Values",
        text: "The actual values stored inside fields (e.g., activity ACTVT = 03 Read-Only or 01 Create, or organization block BUKRS = 1000). Dictates the final permission outcome."
      }}
    }};

    function showSAPNode(box, nodeKey) {{
      document.querySelectorAll('.sap-node-box').forEach(b => b.classList.remove('active'));
      box.classList.add('active');
      
      const data = sapNodes[nodeKey];
      document.getElementById('sap-selected-title').textContent = data.title;
      document.getElementById('sap-selected-text').textContent = data.text;
    }}

    // ════════════════════════════════════════════════════════════════
    // 6. CRAM MATERIAL: DEFINITIONS MATCHER GAME
    // ════════════════════════════════════════════════════════════════
    const MATCH_ALL_PAIRS = [
      {{ term: 'Subject-oriented', def: 'Data Warehouse characteristic: organized around business topics (sales, client).' }},
      {{ term: 'Integrated', def: 'Data Warehouse characteristic: unified data formats from multiple transactional sources.' }},
      {{ term: 'Non-volatile', def: 'Data Warehouse characteristic: historical data is stable and never overwritten.' }},
      {{ term: 'Variant-time', def: 'Data Warehouse characteristic: tracks snapshots and history over time.' }},
      {{ term: 'OLTP', def: 'Online Transaction Processing: handles daily high-speed operations.' }},
      {{ term: 'OLAP', def: 'Online Analytical Processing: supports multi-dimensional analysis in a warehouse.' }},
      {{ term: 'ERP / ERPS', def: 'Enterprise Resource Planning System: integrates and centralizes business data.' }},
      {{ term: 'SAP HANA', def: 'SAP database architecture processing files entirely in fast RAM memory.' }},
      {{ term: 'DSS', def: 'Decision Support System: assists managers with semi-structured decision models.' }},
      {{ term: 'Structured Decision', def: 'Repetitive decision where all calculation steps are known in advance.' }},
      {{ term: 'Unstructured Decision', def: 'Decision requiring raw human judgment and evaluation, cannot be automated.' }},
      {{ term: 'Semi-structured', def: 'Decision where some rules are clear, but manager judgment is still needed.' }},
      {{ term: 'BPM', def: 'Business Performance Management: calculated as Business Intelligence + Planning.' }},
      {{ term: 'KPI', def: 'Key Performance Indicator: quantifiable value measuring organization progress.' }},
      {{ term: 'SaaS', def: 'Cloud model delivering finalized client software via internet (Gmail).' }},
      {{ term: 'IaaS', def: 'Cloud model providing VM hardware, networking, and storage (AWS EC2).' }},
      {{ term: 'PaaS', def: 'Cloud model providing operating system and runtimes for developer builds (Heroku).' }},
      {{ term: 'Competitive Intelligence', def: 'Legal and ethical gathering of competitor data from public sources.' }},
      {{ term: 'SU01', def: 'SAP transaction code used to create and configure user accounts.' }},
      {{ term: 'PFCG', def: 'SAP profile generator transaction code used to manage roles.' }},
      {{ term: '3-Way Match', def: 'Matching Invoice (MIRO) against Purchase Order (PO) and Goods Receipt (GR).' }},
      {{ term: 'ME21N', def: 'SAP transaction code used to create a Purchase Order.' }},
      {{ term: 'MIGO', def: 'SAP transaction code used to post Goods Receipt.' }},
      {{ term: 'MIRO', def: 'SAP transaction code used to log Invoice Verification.' }}
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
        matchSelectedEl.classList.add('matched');
        el.classList.remove('selected');
        el.classList.add('matched');
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
      setCloudModel('prem');
    }};
  </script>
</body>
</html>"""

    # Format JSON strings
    db_json = json.dumps(DATABASE, indent=2)
    
    # Escape TSV content braces
    escaped_anki_tsv = anki_tsv_content.replace('{', '{{').replace('}', '}}')

    # Replace values in the template
    full_html = html_template.replace('{{', '{').replace('}}', '}')
    full_html = full_html.replace('{database_json}', db_json)
    full_html = full_html.replace('{anki_tsv}', escaped_anki_tsv)
    
    # Save the file
    out_path = "d:/CZUU/IS_EXAM_SUITE/EXAM_MASTER_2H.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Successfully generated IS Master Guide at d:/CZUU/IS_EXAM_SUITE/EXAM_MASTER_2H.html")

if __name__ == '__main__':
    generate_html()
