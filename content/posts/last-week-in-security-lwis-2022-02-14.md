Title: Last Week in Security (LWiS) - 2022-02-14
Date: 2022-02-14 22:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-02-14
Author: Erik
Summary: Prevent IP takeover (<a href="https://twitter.com/infosec_au" target="_blank">@infosec_au</a>), Windows LPE via handles (<a href="https://twitter.com/last0x00" target="_blank">@last0x00</a>), Exception Oriented Programming (<a href="https://twitter.com/BillDemirkapi" target="_blank">@BillDemirkapi</a> and <a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), Bloodhound 4.1 (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), object overloading (<a href="https://twitter.com/_xpn_/" target="_blank">@_xpn_</a>), arb file write on DCs (<a href="https://twitter.com/Junior_Baines" target="_blank">@Junior_Baines</a>), KrbRelay (<a href="https://twitter.com/cube0x0" target="_blank">@cube0x0</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-02-07 to 2022-02-14.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://security.googleblog.com/2022/02/roses-are-red-violets-are-blue-giving.html" target="_blank">🌹 Roses are red, Violets are blue 💙 Giving leets 🧑‍💻 more sweets 🍭 All of 2022!</a>. There is big money in Linux Kernel and Kubernetes 0days and 1days these days.</li>
<li><a href="https://portswigger.net/daily-swig/cryptocurrency-firm-makerdao-offers-record-10m-in-newly-launched-bug-bounty-program" target="_blank">Cryptocurrency firm MakerDAO offers record $10m in newly launched bug bounty program</a>. The real money is in hacking smart contracts. Don't believe me? <a href="https://rekt.news/leaderboard/" target="_blank">You should</a>.</li>
<li><a href="https://krcgtv.com/news/local/no-charges-for-st-louis-post-dispatch-reporter-who-found-database-flaw" target="_blank">Prosecutor will not charge Post-Dispatch for DESE data vulnerability story</a>. Four months after a reporter used "view-source" to find social security numbers on a state run school website, the county prosecutor said he will not prosecute. A bit crazy it had to go all the way to a prosecutor before someone had enough sense to shut it down.</li>
<li><a href="https://www.ncsc.gov.uk/files/2021%20Trends%20show%20increased%20globalised%20threat%20of%20ransomware.pdf" target="_blank">2021 Trends Show Increased Globalized Threat of Ransomware (PDF)</a>. NCSC, CISA, and the NSA team up to warn everyone about ransomware. This would be a good release for 2017.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://www.trustedsec.com/blog/object-overloading/" target="_blank">Object Overloading</a>. This is a dense but very interesting article. TLDR is you can convince processes to load DLLs from directories on start with ProcessDeviceMap, but this isn't an article to skip over. <a href="https://github.com/xpn/ObjectOverloadingPOC" target="_blank">ObjectOverloadingPOC</a> has the code.</li>
<li><a href="https://blog.assetnote.io/2022/02/13/dangling-eips/" target="_blank">Eliminating Dangling Elastic IP Takeovers with Ghostbuster</a>. IP takeovers can be dangerous (see <a href="https://caniphish.com/phishing-resources/blog/compromising-australian-supply-chains-at-scale" target="_blank">compromising the email supply chain of Australia's most respected institutions</a> -also AUS based 🤔), so shubs developed <a href="https://github.com/assetnote/ghostbuster" target="_blank">ghostbuster</a> which scans all your cloud assigned IPs, then checks if there are any DNS records pointing to IPs you don't have control over.</li>
<li><a href="https://aptw.tf/2022/02/10/leaked-handle-hunting.html" target="_blank">Gaining the upper hand(le)</a>. Sometimes SYSTEM level processes on Windows spawn lower integrity processes but keep high integrity handles open. This post shows how that can be exploited and teases a tool that does it all automatically. No release yet though.</li>
<li><a href="https://billdemirkapi.me/exception-oriented-programming-abusing-exceptions-for-code-execution-part-1/" target="_blank">Abusing Exceptions for Code Execution, Part 1</a>. This is a similar post to <a href="https://www.x86matthew.com/view_post?id=windows_no_exec" target="_blank">WindowsNoExec</a>, but with more detail and macOS <a href="https://github.com/D4stiny/ExceptionOrientedProgramming" target="_blank">PoC</a> to boot. Exception oriented programming (EOP) is the future?</li>
<li><a href="https://www.blackarrow.net/ad-cs-from-manageca-to-rce/" target="_blank">AD CS: from ManageCA to RCE</a>. ManageCA and ManageCertificates permissions were suggested to be dangerous in the <a href="https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf" target="_blank">Certified Pre-Owned (PDF)</a> paper, but now a user with the ManageCA permission has the ability to perform an arbitrary file write on any local path on the CA server or on any remote path where that server has write permissions, and thus RCE. Check the BlackArrow <a href="https://github.com/blackarrowsec/Certify" target="_blank">Certify</a> for the new features.</li>
<li><a href="https://malacupa.com/2022/02/08/active-directory-whoami.html" target="_blank">Active Directory, whoami?</a>. Last week there was a tool release (<a href="https://github.com/bugch3ck/SharpLdapWhoami" target="_blank">SharpLdapWhoami</a>) I didn't fully understand the use for. A helpful reader spelled it out for me!</li>
<li><a href="https://posts.specterops.io/introducing-bloodhound-4-1-the-three-headed-hound-be3c4a808146" target="_blank">Introducing BloodHound 4.1 — The Three Headed Hound</a>. Three new edges arrive in 4.1: AddKeyCredentialLink, AddSelf, and WriteSPN. Read the post to learn about each of them.</li>
<li><a href="https://www.x86matthew.com/view_post?id=stack_scraper" target="_blank">StackScraper - Capturing sensitive data using real-time stack scanning against a remote process</a>. This memory searching tool could be very useful for post-exploitation credential harvesting, or app security research.</li>
<li><a href="https://www.rapid7.com/blog/post/2022/02/14/dropping-files-on-a-domain-controller-using-cve-2021-43893/" target="_blank">Dropping Files on a Domain Controller Using CVE-2021-43893</a>. The December patch tuesday patch for CVE-2021-43893 (remote privesc against encrypted file systems (EFS)) was't completely patched. Jake from Rapid7 decided to weaponize it and on top of authenticated users being able to write arbitrary files to a DC, the incomplete patch allows for yet another authentication elicitation technique. Sprinkle on some relaying, and before you know it you're authenticated as a DA's machine account (if a machine account in in the DA group that is)! The tool is called <a href="https://github.com/jbaines-r7/blankspace" target="_blank">blankspace</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/cube0x0/KrbRelay" target="_blank">KrbRelay</a> is a framework for Kerberos relaying. The relaying game just got a whole lot more interesting. The <a href="https://github.com/cube0x0/KrbRelay/blob/main/Images/demo.mp4" target="_blank">demo</a> is very impressive.</li>
<li><a href="https://github.com/Flangvik/CobaltBus" target="_blank">CobaltBus</a> is a Cobalt Strike External C2 Integration With Azure Servicebus, C2 traffic via Azure Servicebus.</li>
<li><a href="https://github.com/ChadMotivation/TymSpecial" target="_blank">TymSpecial</a> is a SysWhispers integrated shellcode loader w/ ETW patching, anti-sandboxing, &amp; spoofed code signing certificates</li>
<li><a href="https://github.com/Allevon412/PPL_Sandboxer" target="_blank">PPL_Sandboxer</a> is a A small C POC to make Defender Useless by removing Token privileges and lowering Token Integrity.</li>
<li><a href="https://github.com/ly4k/SpoolFool" target="_blank">SpoolFool</a> is an exploit for CVE-2022-21999 - Windows Print Spooler Elevation of Privilege Vulnerability (LPE) that should work by default on all Windows desktop versions up to the 2022-02-08 patch.</li>
<li><a href="https://github.com/Deputation/hygieia" target="_blank">hygieia</a> is a vulnerable driver traces scanner written in C++ as an x64 Windows kernel driver.</li>
<li><a href="https://github.com/mufeedvh/pdfrip" target="_blank">pdfrip</a> is a fast PDF password cracking utility equipped with commonly encountered password format builders and dictionary attacks.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/bonjourmalware/melody/" target="_blank">melody</a> is a transparent internet sensor built for threat intelligence. Supports custom tagging rules and vulnerable application simulation.</li>
<li><a href="https://monorepo.tools/?ck_subscriber_id=196141537" target="_blank">monorepo.tools</a>. "Everything you need to know about monorepos, and the tools to build them." With a bit of nudging to use Nx because the team the wrote this is selling Nx (but honestly Nx looks pretty awesome).</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
