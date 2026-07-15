Title: Last Week in Security (LWiS) - 2020-10-26
Date: 2020-10-26 19:30
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-10-26
Author: Erik
Summary: LOLBin post from <a href="https://twitter.com/bohops" target="_blank">@bohops</a>, new Excel macro tool from <a href="https://twitter.com/JoeLeonJr" target="_blank">@JoeLeonJr</a>, Windows sandbox detection by <a href="https://twitter.com/LloydLabs" target="_blank">@LloydLabs</a>, macOS LPE by <a href="https://twitter.com/0xm1rch" target="_blank">@0xm1rch</a>, how to use Azure passwords by <a href="https://twitter.com/kfosaaen" target="_blank">@kfosaaen</a>, a review of low cost pentests by <a href="https://twitter.com/_sophron" target="_blank">@_sophron</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-10-19 to 2020-10-26.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.justice.gov/opa/press-release/file/1328521/download" target="_blank">US charges Russian hackers behind NotPetya, KillDisk, OlympicDestroyer attacks</a>. This indictment isn't groundbreaking for its attribution of the 3 attacks to Russian hackers (that was widely assumed), it is however very interesting to see the evidence for such attribution. Clearly, the US government has a lot of access to some of the backends used by the hackers. Bravo. For excerpts, see <a href="https://twitter.com/RidT/status/1318247254327758849" target="_blank">this twitter thread</a>.</li>
<li><a href="https://www.vmware.com/security/advisories/VMSA-2020-0023.html" target="_blank">Multiple vulnerabilities in VMware ESXi</a>. No PoCs yet but this is a potential unauthenticated remote code execution vulnerability in the OpenSLP service on ESXi (port 427).</li>
<li><a href="https://objective-see.com/blog/blog_0x4E.html" target="_blank">Apple Approved Malware</a>. Malware is being deployed using binaries that are notarized (signed) by Apple after passing their review process. This wouldn't be as bad if the signed samples weren't known malware! Additionally, after reporting one sample, the actors simply updated their campaign with a freshly signed sample of the same thing. Clearly, the actors involved have the notarization process figured out and automated. This is a bad look for Apple who tout this notarization feature as a big security selling point.</li>
<li><a href="https://github.com/NanoAdblocker/NanoCore/issues/362" target="_blank">Recent and upcoming changes to the Nano projects</a>. Popular ad blocker NanoCore was recently sold to a Turkish developer who immediately changed the privacy policy and modified the code. Browser extensions command great power, and should be carefully scrutinized.</li>
<li><a href="https://blog.1password.com/1password-for-linux-beta-is-now-open/" target="_blank">1Password for Linux beta is now open</a>. One of the more popular password managers is now available on linux (in beta). For an open source alternative that is available on linux today, check out <a href="https://bitwarden.com/download/" target="_blank">Bitwarden</a>.</li>
<li><a href="https://news.perthchat.org/youtube-dl-removed-from-github/" target="_blank">YouTube-DL Removed From GitHub After DMCA Notice</a>. This is an incredibly useful tool with a wide range of legitimate uses. The complaint says the code <em>can</em> be used to download copyrighted works. This sets a precedent that makes posting software or tools that <em>can</em> be used for malicious acts (nearly everything in every LWiS) potentially subject to take down as well (for ToS violations not DCMA). Looks like people are already using a GitHub "feature" to <a href="https://github.com/github/dmca/tree/416da574ec0df3388f652e44f7fe71b1e3a4701f" target="_blank">attach a commit of youtube-dl to the DCMA repo</a> (and of course forks like <a href="https://github.com/blackjack4494/yt-dlc" target="_blank">yt-dlc</a> exist).</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://sophron.github.io/lowcost-freelancing-pentest/" target="_blank">Penetration Testing and Low-Cost Freelancing</a>. This post looks at some low cost penetration testing offerings. Like in everything, you get what you pay for. This is a good piece to argue for more funding for higher quality assessments.</li>
<li><a href="https://www.mdsec.co.uk/2020/10/segmentation-vault/" target="_blank">Segmentation Vault: Cloning Thick Client Access</a>. This post discusses a practical method for red teams to compromise thick client applications when they store credential material in “Vault”, using Microsoft OneDrive as an example. This could be useful to download files "out of band" (not using your C2) or to maintain access to OneDrive if access to the target machine is lost.</li>
<li><a href="https://bohops.com/2020/10/21/exploring-an-assembly-loading-technique-and-detection-mechanism-for-the-gfxdownloadwrapper-exe-lolbin/" target="_blank">Exploring an Assembly Loading Technique and Detection Mechanism for the GfxDownloadWrapper.exe LOLBIN</a>. GfxDownloadWrapper.exe is a binary that is included with Intel video card driver software, and older version could download arbitrary files as well as execute DLLs. This post show how these features were discovered and how defenders can detect their use.</li>
<li><a href="https://blog.netspi.com/a-beginners-guide-to-gathering-azure-passwords/" target="_blank">A Beginners Guide to Gathering Azure Passwords</a>. As cloud adoption grows, red teamers have to adapt. This blog post describes different Azure service and what they have access to. This information comes from the authors of the amazing <a href="https://github.com/Netspi/Microburst" target="_blank">MicroBurst</a> tool.</li>
<li><a href="https://decoder.cloud/2020/10/24/when-ntuser-pol-leads-you-to-system/" target="_blank">When ntuser.pol leads you to SYSTEM</a> shows a bypass (now patched) to <a href="https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-1317" target="_blank">CVE-2020-1317</a>, a group policy local privilege escalation bug for Windows.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/slaeryan/AQUARMOURY/tree/master/Wraith" target="_blank">Wraith</a> is a native loader designed to pave the way for the arrival of a Stage-1/Beaconing implant or Stage-2/Post-Ex implant in-memory securely and stealthily. Specially designed to operate in heavily-monitored environments, it is designed with AV Evasion as its primary goal.</li>
<li><a href="https://iwantmore.pizza/posts/PEzor2.html" target="_blank">PEzor v2 — New Output Formats and Cobalt Strike Integration</a>. PEzor was already a great tool, and v2 includes new features like a nice <a href="https://github.com/phra/PEzor/blob/master/aggressor/PEzor.cna" target="_blank">cna</a> script to make in-memory execute of nearly any binary a single command. If you haven't checked this out before v2, it is even more valuable now.</li>
<li><a href="https://fortynorthsecurity.com/blog/hot-manchego/" target="_blank">Hot Manchego</a> is a new tool for creating macro-enabled Excel workbooks that use the .NET library EPPlus to bypass many AV solutions.</li>
<li><a href="https://www.ambionics.io/blog/symfony-secret-fragment" target="_blank">Secret fragments: Remote code execution on Symfony based websites</a>. The <cite>_fragment</cite> endpoint used by Symofny (and therefore lots of PHP based web apps/CMSs) uses an HMAC to verify commands. Unfortunately, lots of sites are using default keys to generate the HMAC, and are therefore vulnerable to RCE. PoC <a href="https://github.com/ambionics/symfony-exploits" target="_blank">here</a>.</li>
<li><a href="https://github.com/mdsecactivebreach/RegistryStrikesBack" target="_blank">RegistryStrikesBack</a> allows a red team operator to export valid .reg files for portions of the Windows Registry via a .NET assembly that should run as a standard user. See <cite>Segmentation Vault</cite> in Techniques for example usage.</li>
<li><a href="https://github.com/mdsecactivebreach/CloneVault" target="_blank">CloneVault</a> allows a red team operator to export and import entries including attributes from Windows Credential Manager. This allows for more complex stored credentials to be exfiltrated and used on an operator system. See <cite>Segmentation Vault</cite> in Techniques for example usage.</li>
<li><a href="https://www.gosecure.net/blog/2020/10/20/announcing-pyrdp-1/" target="_blank">Announcing PyRDP 1.0</a>. The advanced RDP python library gains features as it reaches 1.0 including CredSSP, Clipboard file carving, headless player support, dynamic certificate cloning, and a new conversion tool to output mp4 videos of RDP sessions from PyRDP captures or even PCAPs.</li>
<li><a href="https://github.com/S1lkys/CVE-2020-15906" target="_blank">CVE-2020-15906</a> is an authentication bypass for TikiWiki CMS 16.x-21.1. This wiki software is often used internally by dev shops, so this vulnerability could prove very useful on internal engagements. Demo <a href="https://youtu.be/o3blz2US54Y" target="_blank">here</a>.</li>
<li><a href="https://github.com/LloydLabs/wsb-detect" target="_blank">wsb-detect</a> enables you to detect if you are running in Windows Sandbox ("WSB"). The sandbox is used by Windows Defender for dynamic analysis, and commonly manually by security analysts and alike.</li>
<li><a href="https://github.com/tyranid/setsidmapping" target="_blank">setsidmapping</a> is a tool to use LsaManageSidNameMapping get LSA to add or remove SID to name mappings. It requires SeTcbPrivilege as well as some other caveats. Not sure what advantages this provides right now, but I'm sure James is cooking up something with this tool.</li>
<li><a href="https://github.com/vp777/procrustes" target="_blank">procrustes</a> is a bash script that automates the exfiltration of data over dns in case you have  blind command execution on a server where all outbound connections except DNS are blocked.</li>
<li><a href="https://github.com/GoSecure/WSuspicious/" target="_blank">WSuspicious</a> is a proof of concept program to escalate privileges on a Windows host by abusing WSUS. Details in <a href="https://www.gosecure.net/blog/2020/09/08/wsus-attacks-part-2-cve-2020-1013-a-windows-10-local-privilege-escalation-1-day/" target="_blank">this blog post</a>.</li>
<li><a href="https://www.criticalstart.com/local-privilege-escalation-vulnerability-discovered-in-vmware-fusion/" target="_blank">Local Privilege Escalation Vulnerability Discovered in VMware Fusion</a>. A nice macOS privilege escalation using VMware Fusion. The bug was patched in September but the PoC is fresh. Code <a href="https://github.com/Critical-Start/Team-Ares/blob/master/CVE-2020-3980/CVE-2020-3980.sh" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/mlgualtieri/NTLMRawUnHide" target="_blank">NTLMRawUnHide</a> is a Python3 script designed to parse network packet capture files and extract NTLMv2 hashes in a crackable format. The following binary network packet capture formats are supported: *.pcap *.pcapng *.cap *.etl.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
