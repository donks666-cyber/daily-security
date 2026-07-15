Title: Last Week in Security (LWiS) - 2023-05-01
Date: 2023-05-01 21:15
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-05-01
Author: Erik
Summary: ML packer classification (<a href="https://twitter.com/accidentalrebel" target="_blank">@accidentalrebel</a>), DLL unlinking (<a href="https://infosec.exchange/@christophetd" target="_blank">@christophetd@infosec.exchange</a>), Apache Superset and Papercut RCEs (<a href="https://twitter.com/Horizon3Attack" target="_blank">@Horizon3Attack</a>), SushiSwap hack (<a href="https://twitter.com/Dooflin5" target="_blank">@Dooflin5</a>), macOS LPE (<a href="https://twitter.com/patch1t" target="_blank">@patch1t</a>), macros in 2023 (<a href="https://twitter.com/ptrpieter" target="_blank">@ptrpieter</a>), nanodump update (<a href="https://twitter.com/s4ntiago_p" target="_blank">@s4ntiago_p</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-04-17 to 2023-05-01.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://citizenlab.ca/2023/04/nso-groups-pegasus-spyware-returns-in-2022/" target="_blank">Triple Threat: NSO Group's Pegasus Spyware Returns in 2022 with a Trio of iOS 15 and iOS 16 Zero-Click Exploit Chains</a>. Good thing we have <a href="https://www.macrumors.com/2023/05/01/rapid-security-response-16-4-1/" target="_blank">Rapid Security Response</a>?</li>
<li><a href="https://security.googleblog.com/2023/04/google-authenticator-now-supports.html" target="_blank">Google Authenticator now supports Google Account synchronization</a>. This was a huge downside to using the Goole provided MFA code generation app. Lost, stolen, or simple device upgrades were a struggle. I have been pushing <a href="https://raivo-otp.com/" target="_blank">Raivo OTP</a>, an open source MFA app with encrypted seed synicning support because of the drawbacks for Google's own app. They release says that the new sync feature makes MFA codes "more durable by storing them safely in users' Google Account," but does not explicitly say if the seeds will be symetrically encrypted. Does this open a new level of compromise to Google Account takeovers? Can attackers sync the seeds to a device without an authenticator specific password? Like always, FIDO2 keys and <a href="https://landing.google.com/advancedprotection/" target="_blank">Advanced Protection</a> are the answer.</li>
<li><a href="https://mullvad.net/en/blog/2023/4/20/mullvad-vpn-was-subject-to-a-search-warrant-customer-data-not-compromised/" target="_blank">Mullvad VPN was subject to a search warrant. Customer data not compromised</a>. The feds showed up with a warrant, but left without taking anything. Commercial VPNs have a very narrow use case, and if your threat model warrents one, you probably shouldn't trust any one provider.</li>
<li><a href="https://krebsonsecurity.com/2023/04/3cx-breach-was-a-double-supply-chain-compromise/" target="_blank">3CX Breach Was a Double Supply Chain Compromise</a>. Yo dawg, I heard you like supply chain compromises...</li>
<li><a href="https://github.blog/2023-04-25-git-security-vulnerabilities-announced-4/" target="_blank">Git security vulnerabilities announced</a>. No surprise that GitHub found some git vulnerabilities. Update your git clients today!</li>
<li><a href="https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-remote-command-injection-vulnerability-of-firewalls" target="_blank">Zyxel security advisory for OS command injection vulnerability of firewalls</a>. Unauthenticated remote command execution in a firewall... You had one job.</li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2023/04/18/microsoft-shifts-to-a-new-threat-actor-naming-taxonomy/" target="_blank">Microsoft shifts to a new threat actor naming taxonomy</a>. Ah yes... <a href="https://xkcd.com/927/" target="_blank">Standards</a>.</li>
<li><a href="https://blog.whatsapp.com/an-open-letter" target="_blank">An open letter</a>. The UK's <a href="https://www.gov.uk/guidance/a-guide-to-the-online-safety-bill" target="_blank">Online Safety Bill</a> could destroy end-to-end encryption in the UK. Privacy is a <a href="https://www.refworld.org/docid/453883f922.html" target="_blank">human right</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.synacktiv.com/en/publications/windows-secrets-extraction-a-summary.html" target="_blank">Windows secrets extraction: a summary</a>. Excellent overview of the current state of windows credential material extraction.</li>
<li><a href="https://www.synacktiv.com/en/publications/i-hack-u-boot.html" target="_blank">I hack, U-Boot</a>. A very detailed and technical post on the most common bootloader in the embedded space.</li>
<li><a href="https://www.accidentalrebel.com/classifying-malware-packers-using-machine-learning.html" target="_blank">Classifying Malware Packers Using Machine Learning</a>. ML models have gotten very good at clasifying images (thanks im part to your capcha clicks), why not covert binaries to images and have the ML classify them?</li>
<li><a href="https://blog.christophetd.fr/dll-unlinking/" target="_blank">Hiding in Plain Sight: Unlinking Malicious DLLs from the PEB</a>. This won't be effective against EDR in the kernel (Defender, Crowdstrike, etc), but could be useful to hide from userspace detections.</li>
<li><a href="https://fortynorthsecurity.com/blog/proxy-vm-traffic-through-burp-suite/" target="_blank">How to Proxy VM Traffic through Burp Suite</a>. A simple trick, but if you weren't aware of the system wide proxy setting in Windows, this is a useful tip.</li>
<li><a href="https://security.googleblog.com/2023/04/securely-hosting-user-data-in-modern.html" target="_blank">Securely Hosting User Data in Modern Web Applications</a>. Ever wonder why domains like <cite>githubusercontent.com</cite> or <cite>googleusercontnet.com</cite> exist? For your protection!</li>
<li><a href="https://www.horizon3.ai/cve-2023-27524-insecure-default-configuration-in-apache-superset-leads-to-remote-code-execution/" target="_blank">CVE-2023-27524: Insecure Default Configuration in Apache Superset Leads to Remote Code Execution</a>. Always change the default key values! Developers, generate random values on first startup to prevent this.</li>
<li><a href="https://www.horizon3.ai/papercut-cve-2023-27350-deep-dive-and-indicators-of-compromise/" target="_blank">PaperCut CVE-2023-27350 Deep Dive and Indicators of Compromise</a>. If only all patch diffs were this simple. Good write up from initial news to full RCE.</li>
<li><a href="https://maxwelldulin.com/BlogPost?post=3971654656" target="_blank">Eating 4 Day Old Sushi - Replicating the SushiSwap Hack</a>. DeFi continues to be the ultimate black hat bug bounty.</li>
<li><a href="https://jhftss.github.io/CVE-2023-23525-Get-Root-via-A-Fake-Installer/" target="_blank">CVE-2023-23525: Get Root via A Fake Installer</a>. Fake installers could use the permission granted by users during install to gain root access. Update to macOS 13.3 to apply the fix.</li>
<li><a href="https://blog.assetnote.io/2023/04/26/xss-million-websites-cpanel/" target="_blank">Finding XSS in a million websites (cPanel CVE-2023-29489)</a>. Good web vulnerability hunting process in this post. If you liked that you'll also enjoy <a href="https://blog.assetnote.io/2023/04/30/rce-oracle-opera/" target="_blank">Exploiting an Order of Operations Bug to Achieve RCE in Oracle Opera</a>.</li>
<li><a href="https://www.gosecure.net/blog/2023/04/26/never-connect-to-rdp-servers-over-untrusted-networks/" target="_blank">Never Connect to RDP Servers Over Untrusted Networks</a>. You can collect Net-NTLMv2 without showing a certificate warning (MitM) to the user. Microsoft says this is "by design" and won't fix it.</li>
<li><a href="https://labs.nettitude.com/blog/creating-an-ir-nightmare-drop-box/" target="_blank">Creating an IR Nightmare Drop Box</a>. A good drop box can be crucial to success on a physical engagement. For bonus points, wire this up with <a href="https://labs.nettitude.com/blog/using-lora-as-a-side-channel/" target="_blank">LoRa as a Side Channel</a>.</li>
<li><a href="https://outflank.nl/blog/2023/04/25/so-you-think-you-can-block-macros/" target="_blank">So you think you can block Macros?</a>. Macros aren't quite dead yet. Turns out it's pretty hard to completely lock down an arbitrary scripting system that enterprises rely on for business.</li>
<li><a href="https://blog.ryotak.net/post/github-actions-staff-access-token-en/" target="_blank">Stealing GitHub staff's access token via GitHub Actions</a>. A ten second sleep was all it took to steal some access tokens. Well done!</li>
<li><a href="https://suspicious.actor/misc/2023/04/27/nighthawk-memory-obfuscation.html" target="_blank">NightHawk Memory Obfuscation</a>. What's old is new again. <a href="https://github.com/realoriginal/titanldr-ng" target="_blank">titanldr-ng</a> has a Cobalt Strike compatible variant (check out Obf.c).</li>
<li><a href="https://the-deniss.github.io/posts/2023/04/26/avast-privileged-arbitrary-file-create-on-quarantine.html" target="_blank">Avast Anti-Virus privileged arbitrary file create on virus quarantine (CVE-2023-1585 and CVE-2023-1587)</a>. You either die a hero or...</li>
<li><a href="https://vanmieghem.io/process-injection-evading-edr-in-2023/" target="_blank">Process injection in 2023, evading leading EDRs</a>. Vincent always drops succinct, high quality content.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://posts.specterops.io/introducing-bloodhound-4-3-get-global-admin-more-often-5795cbf535b2" target="_blank">Introducing BloodHound 4.3 — Get Global Admin More Often</a>. More Azure and MS Graph features!</li>
<li><a href="https://github.com/optiv/ScareCrow/releases/tag/v5.0" target="_blank">ScareCrow</a>. Not a new tool but a big update to the payload creation framework for v5.0.</li>
<li><a href="https://github.com/fortra/nanodump" target="_blank">nanodump</a> - Not new, but the recent updates allows for PPL dumping!</li>
<li><a href="https://github.com/3NailsInfoSec/DCVC2" target="_blank">DCVC2</a> - A Golang Discord C2 unlike any other. DCVC2 uses RTP packets over a voice channel to transmit all data leaving no operational traces in text chats.</li>
<li><a href="https://github.com/JakeWnuk/maskcat" target="_blank">maskcat</a> - Utility tool for Hashcat Masks and Password Cracking.</li>
<li><a href="https://github.com/redcanaryco/mac-monitor" target="_blank">mac-monitor</a> - Red Canary Mac Monitor is an advanced, stand-alone system monitoring tool tailor-made for macOS security research. Beginning with Endpoint Security (ES), it collects and enriches system events, displaying them graphically, with an expansive feature set designed to reduce noise.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/highlight/highlight" target="_blank">highlight</a> - highlight.io: The open source, full-stack monitoring platform. Error monitoring, session replay, logging and more. I haven't seen a self-hostable web session recording system before highlight.</li>
<li><a href="https://github.com/Orange-Cyberdefense/KeePwn" target="_blank">KeePwn</a> - A python tool to automate KeePass discovery and secret extraction.</li>
<li><a href="https://www.zackproser.com/blog/maintaining-this-site-fucking-sucks" target="_blank">Maintaining this site fucking sucks</a>. This guy needs my blog CI/CD pipeline. When I finish a blog post it's one command to publish it and set up the env for next week. Maybe, just maybe, you don't need all that javascript (hint: there isn't a single line of functional javascript on this site).</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 424 (+0)</p>
<p>Blogs monitored: 339 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
