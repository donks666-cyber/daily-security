Title: Last Week in Security (LWiS) - 2026-03-24
Date: 2026-03-24 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2026-03-24
Author: Erik
Summary: The FCC bans all new foreign routers, Delve was a compliance as a service scam, ForceHound, VMKatz, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2026-03-16 to 2026-03-24.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service" target="_blank">Delve - Fake Compliance as a Service - Part I</a> - As someone who has dealt with compliance, the desire to have a one stop company deliver the end result is tempting, and the SOC 2 standard allowed for this abuse. When the "auditors" are being paid by the company being audited this is the inevitable outcome. Delve just took it to the extreme and made rubber stamping a service.</li>
<li><a href="https://www.fcc.gov/sites/default/files/NSD-Routers0326.pdf" target="_blank">[PDF] National Security Determination on the Threat Posed by Routers Produced by Foreign Countries</a> - All new "routers produced in a foreign country, regardless of the nationality of the producer" are now banned in the US because malicious actors had exploited security gaps in foreign-made routers "to attack households, disrupt networks, enable espionage, and facilitate intellectual property theft." If you're going to ban based on "national security" concerns, limiting consumer freedom, you should be able to share solid evidence of the concerns with the public. Four links to APT/botnet reports does not demonstrate that producing a router in the US will protect them from exploitation. "Entities that produce routers in a foreign country are encouraged to apply for Conditional Approvals." Oh, they just want bribes. Neat.</li>
<li><a href="https://x.com/darkwebinformer/status/2036195002510880911" target="_blank">[X] Unconfirmed breach of OVHcloud</a> - What threat actor posting data for sale on BreachForums has 530TB of empty storage space for this exfil? Are they using a 3rd party cloud service for storage (encrypted data one assumes)?</li>
<li><a href="https://ramimac.me/trivy-teampcp/" target="_blank">Trivy Supply Chain Compromise</a> - What happens when your security scanner is compromised with a credential stealer? The blast radius on this one was bad. It may have been related to/the cause of the <a href="https://www.netspi.com/blog/executive-blog/ai-ml-pentesting/litellm-supply-chain-compromise/" target="_blank">LiteLLM</a> compromise?</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://itm4n.github.io/cve-2026-20817-wersvc-eop/" target="_blank">CVE-2026-20817 - Windows Error Reporting Service EoP</a> - The <a href="https://github.com/itm4n/CVEs/tree/master/CVE-2026-20817" target="_blank">proof-of-concept</a> doesn't quite pop a SYSTEM shell, but it gets close (having WerFault.exe run with user controlled command line arguments).</li>
<li><a href="https://labs.watchtowr.com/a-32-year-old-bug-walks-into-a-telnet-server-gnu-inetutils-telnetd-cve-2026-32746/" target="_blank">A 32-Year-Old Bug Walks Into A Telnet Server (GNU inetutils Telnetd CVE-2026-32746 Pre-Auth RCE)</a> - A bug from 1994 was finally patched. I wonder if some 60+ year old hacker just had their 32 year old 0day burned.</li>
<li><a href="https://blog.amberwolf.com/blog/2026/march/patch-bypass---netskope-client-for-windows---local-privilege-escalation-via-rogue-server/" target="_blank">Patch Bypass: Netskope Client for Windows - Local Privilege Escalation via Rogue Server</a> - Using the provider's own reverse proxy service to tunnel your exploit through their infrastructure and thus bypass the url checks is devious.</li>
<li><a href="https://certitude.consulting/blog/en/abusing-modern-browser-features-for-phishing/" target="_blank">Abusing Modern Browser Features for Phishing</a> - With some tweaking this could be very effective.</li>
<li><a href="https://flatt.tech/research/posts/remote-command-execution-in-google-cloud-with-single-directory-deletion/" target="_blank">Remote Command Execution in Google Cloud with Single Directory Deletion</a> - Not often do we see a remote code execution in a major cloud provider service.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/bu5h-d/ludus_kubernetes_goat" target="_blank">ludus_kubernetes_goat</a> - Ansible role that deploys Kubernetes Goat on a <a href="https://ludus.cloud" target="_blank">Ludus</a> range VM using k3s and Helm</li>
<li><a href="https://github.com/mojeda101/ludus_kali_setup" target="_blank">ludus_kali_setup</a> - An Ansible role that bootstraps a Kali Linux VM in a <a href="https://ludus.cloud" target="_blank">Ludus</a> range with some more preferable settings for demo and lab usage.</li>
<li><a href="https://github.com/joaoh82/rustunnel" target="_blank">rustunnel</a> - is a open-source tunnel service written in Rust that replicates the core functionality of ngrok. It exposes local services running behind NAT/firewalls to the public internet through a relay server self-hosted or our managed service.</li>
<li><a href="https://github.com/brmkit/toastnotify-bof" target="_blank">toastnotify-bof</a> - A Beacon Object File (BOF) for sending Windows toast notifications. Pairs with the blog post (<a href="https://brmk.me/2026/03/18/toast-my-way.html" target="_blank">toast my way</a> ) for full context and use cases.</li>
<li><a href="https://komo.do/" target="_blank">Komodo</a> - The best (personal option) docker management system released 2.0 with support for swarm management.</li>
<li><a href="https://github.com/nikaiw/VMkatz" target="_blank">VMkatz</a> - Extract Windows credentials directly from VM memory snapshots and virtual disks.</li>
<li><a href="https://github.com/jalvarezz13/Krb5RoastParser" target="_blank">Krb5RoastParser</a> - KrbRoastParser is a tool for parsing Kerberos packets from pcap files to extract AS-REQ, AS-REP and TGS-REP hashes</li>
<li><a href="https://github.com/mhdgning131/teletunnel" target="_blank">teletunnel</a> - Bypassing EDR's with stealthy c++ telegram Bot and Telegram itself as C2 interface</li>
<li><a href="https://github.com/NetSPI/ForceHound" target="_blank">ForceHound</a> - Salesforce identity and permission graph collector for BloodHound CE. Maps users, profiles, permission sets, roles, groups, sharing rules, connected apps, and field-level security into attack-path graphs.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://core-jmp.org/2026/03/can-it-resolve-doom-game-engine-in-2000-dns-records/" target="_blank">Can it Resolve DOOM? Game Engine in 2,000 DNS Records</a> - People really will port DOOM to anything.</li>
<li><a href="https://www.synacktiv.com/en/publications/deep-dive-into-the-deployment-of-an-on-premise-low-privileged-llm-server" target="_blank">Deep-Dive Into the Deployment of an On-Premise Low-Privileged LLM Server</a> - Some nitty gritty sysadmin work.</li>
<li><a href="https://malus.sh/index.html" target="_blank">MALUS - Liberate Open Source</a> - "Clean Room as a Service" 🤣 "Some will argue that what we do is exploitative, that we are extracting the ideas from open source while leaving behind the people who contributed them. To this I say: yes, that is a reasonably accurate description of our business model. It is also a reasonably accurate description of every company that has ever used open source software without contributing back, which is to say, virtually every company that has ever used open source software." 🔥 This is a very well done satire.</li>
<li><a href="https://github.com/Crosstalk-Solutions/project-nomad" target="_blank">project-nomad</a> - Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 496 (+0)</p>
<p>Blogs monitored: 443 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>X: <a href="https://x.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
