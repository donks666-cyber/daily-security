Title: Last Week in Security (LWiS) - 2022-02-28
Date: 2022-02-28 23:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-02-28
Author: Erik
Summary: Stealing GitHub secrets (<a href="https://twitter.com/not_an_aardvark" target="_blank">@not_an_aardvark</a>), TeamsImplant (<a href="https://twitter.com/allevon412" target="_blank">@allevon412</a>), Nimcrypt2 (<a href="https://twitter.com/icyguider" target="_blank">@icyguider</a>), VMware RCEs (<a href="https://twitter.com/elk0kc" target="_blank">@elk0kc</a>), LdapSignCheck (<a href="https://twitter.com/cube0x0" target="_blank">@cube0x0</a>), yaradbg.dev (<a href="https://twitter.com/DissectMalware" target="_blank">@DissectMalware</a>), and more!

<aside class="m-note m-warning">
<h3>Spring Break</h3>
<p>Last Week in Security will be taking a week off next week.</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-02-21 to 2022-02-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://twitter.com/MalwareTechBlog/status/1497829395251171329" target="_blank">LAPSUS$ vs Nvidia</a>. Ransomware crews just aren't what they used to be...</li>
<li><a href="https://twitter.com/ESETresearch/status/1496581903205511181" target="_blank">New data wiper malware used in Ukraine</a>. The use of a <a href="https://opencorporates.com/companies/cy/HE419469" target="_blank">stolen or shell company</a> digital signature as well as an old but legitimate driver to corrupt data is an interesting twist on the common wiper malware methods.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://blog.teddykatz.com/2022/02/23/ghosts-of-branches-past.html" target="_blank">Stealing a few more GitHub Actions secrets</a>. GitHub actions have been a source of secrets before, but this is a very clever logic bug that allowed a malicious fork write access to a repository.</li>
<li><a href="https://connormcgarr.github.io/kuser-shared-data-changes-win-11/" target="_blank">Exploit Development: ASLR - Coming To A KUSER_SHARED_DATA Structure Near You!</a>. Connor drops another monster post digging deep into the Windows kernel to show a new feature in the Windows Insider Preview builds. Kernel exploits will now require a full kASLR bypass to be effective, and existing exploits that rely on a writeable KUSER_SHARED_DATA structure will break.</li>
<li><a href="https://research.nccgroup.com/2022/02/28/brokenprint-a-netgear-stack-overflow/" target="_blank">BrokenPrint: A Netgear stack overflow</a>. Lots of good 32 bit ARM exploitation knowledge in this post.</li>
<li><a href="https://swarm.ptsecurity.com/catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-operations-manager/" target="_blank">Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize Operations Manager</a>. PT security is back with a bunch of different ways to get RCE on VMware products. Some nice web application hacking fundamentals on display in this post.</li>
<li><a href="https://www.shielder.it/advisories/pfsense-remote-command-execution/" target="_blank">Remote Code Execution in pfSense &lt;= 2.5.2</a>. This is an authenticated RCE, but still not good news for a security focused product that's had it's fair share of controversy recently.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/AbdulRhmanAlfaifi/Fennec#compile-with-dependencies-" target="_blank">Fennec</a> is an artifact collection tool written in Rust to be used during incident response on nix based systems. fennec allows you to write a configuration file that contains how to collect artifacts.</li>
<li><a href="https://github.com/Allevon412/TeamsImplant" target="_blank">TeamsImplant</a> is a stealthy teams implant that proxies the urlmon.dll that teams uses compile and throw this bad boy in the teams directory as urlmon.dll and you got yourself a persistence backdoor whenever teams runs by a user or at startup.</li>
<li><a href="https://github.com/awslabs/aws-cloudsaga#running-the-code" target="_blank">aws-cloudsaga</a> is for AWS customers to test security controls and alerts within their Amazon Web Services (AWS) environment, using generated alerts based on security events seen by the AWS Customer Incident Response Team (CIRT).</li>
<li><a href="https://github.com/icyguider/Nimcrypt2#installationdependencies" target="_blank">Nimcrypt2</a> is yet another PE packer/loader designed to bypass AV/EDR. An improvement on the original Nimcrypt project, with the main improvements being the use of direct syscalls and the ability to load regular PE files as well as raw shellcode.</li>
<li><a href="https://github.com/h33tlit/Jbin-website-secret-scraper" target="_blank">Jbin-website-secret-scraper</a> will gather all the URLs from the website and then it will try to expose the secret data from them such as API keys, API secrets, API tokens and many other juicy information.</li>
<li><a href="https://github.com/cube0x0/LdapSignCheck" target="_blank">LdapSignCheck</a> is a Beacon Object File to scan a Domain Controller to see if LdapEnforceChannelBinding or LdapServerIntegrity has been modified to mitigate against relaying attacks.</li>
<li><a href="https://yaradbg.dev/" target="_blank">YaraDbg.dev</a> is a free web-based Yara debugger to help security analysts to write hunting or detection rules with less effort and more confidence. By using YaraDbg, you can perform a thorough root-cause-analysis (RCA) on why some of your Yara rules did or did not match with a specific file. It can also help you to better maintain a large set of yara rules.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/DarkCoderSc/PowerBruteLogon" target="_blank">PowerBruteLogon</a> is a powershell port of <a href="https://github.com/DarkCoderSc/win-brute-logon" target="_blank">win-brute-logon</a> which can brute force local accounts on a Windows machine. The Administrator account, if enabled, is exempt from lockout.</li>
<li><a href="https://github.com/atenreiro/opensquat" target="_blank">opensquat</a> s an opensource Intelligence (OSINT) security tool to identify cyber squatting threats to specific companies or domains, such as Phishing campaigns, Domain squatting, Typo squatting, Bitsquatting, IDN homograph attacks, Doppenganger domains, and Other brand/domain related scams.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
