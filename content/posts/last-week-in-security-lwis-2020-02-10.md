Title: Last Week in Security (LWiS) - 2020-02-10
Date: 2020-02-10 11:40
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-02-10
Author: Erik
Summary: Last Week in Security (LWiS) is a summary of the interesting cyber security news, techniques, tools and exploits from the previous week. This post covers 2020-02-03 to 2020-02-10.

<section id="introduction">
<h2>Introduction</h2>
<p>Cyber security is a fast-paced and ever-changing field. I find myself sifting through countless blogs, subreddits, twitter streams, slack/discord channels, and mailing lists just to stay up to date. I've often thought, "I wish someone would just catalog all the useful/technical/interesting bits in one place, each Monday." So I decided to do just that. It is my intention to make a post similar to this one each Monday, with a collection of the previous weeks news that <em>I</em> found relevant. If you are a technical practitioner of cyber security, perhaps it can be of use to you as well. I plan on automating as much of the information gathering and processing as possible and will blog about that system as it is developed.</p>
</section>
<section id="news">
<h2>News</h2>
<ul>
<li>A Raytheon engineer was arrested for taking US missile defense data to China, a classic example of the insider threat and ITAR violation. <a href="https://www.zdnet.com/article/raytheon-engineer-arrested-for-taking-us-missile-defense-data-to-china/" target="_blank">ZDNet</a> has the story.</li>
<li><a href="http://www.simonweckert.com/googlemapshacks.html" target="_blank">Simon Weckert</a> "hacks" Google Maps with a wagon full of cellphones to create fake traffic jams in Berlin. An interesting and concrete example of potentially adversarial behavior of coordinated users (or just one user acting as multiple) in a distributed system can affect the physical world.</li>
<li>5 Cisco 0days, dubbed <a href="https://www.armis.com/cdpwn/" target="_blank">CDPwn</a>, released.</li>
<li><dl>
<dt>Fireeye published a <a href="https://www.fireeye.com/blog/threat-research/2020/01/stomp-2-dis-brilliance-in-the-visual-basics.html" target="_blank">very in-depth blog post</a> about an actor deploying a backdoor via stomped VBA macro enabled documents.</dt>
<dd><ul>
<li>This <a href="https://twitter.com/JohnLaTwC/status/1226574202250989568" target="_blank">twitter thread</a> is a great resource for more information on VBA stomping, detection, and tools.</li>
</ul>
</dd>
</dl>
</li>
<li>1.7 million dollars can get you access to lots of windows loot; corp.com is for sale and is a prime example of "namespace collision." <a href="https://krebsonsecurity.com/2020/02/dangerous-domain-corp-com-goes-up-for-sale/" target="_blank">Krebs</a> has the details.</li>
<li><dl>
<dt>Ransomware is exploiting vulnerable legitimate signed windows drivers to disable AV before encrypting files. This is an in-the-wild example of signed driver bypass.</dt>
<dd><ul>
<li><a href="https://www.zdnet.com/article/ransomware-installs-gigabyte-driver-to-kill-antivirus-products/" target="_blank">Story</a></li>
<li><a href="https://www.secureauth.com/labs/advisories/gigabyte-drivers-elevation-privilege-vulnerabilities" target="_blank">Disclosure</a></li>
<li><a href="https://github.com/alxbrn/gdrv-loader" target="_blank">Tool (gdrv-loader)</a></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>iOS Exploit News</dt>
<dd><ul>
<li><a href="https://twitter.com/Fox0x01/" target="_blank">@Fox0x01</a> released the <a href="https://azeria-labs.com/grooming-the-ios-kernel-heap/" target="_blank">third part</a> of her iOS exploit development series. Her site is a treasure for anyone in need of an exploit development resource. I highly recommend it.</li>
<li><a href="https://twitter.com/_bazad" target="_blank">Brandon Azad</a>, iOS exploitation master, released "<a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=1986#c4" target="_blank">oob_timestamp</a>," a proof-of-concept research exploit that exports the kernel task port on iOS 13.3. Amazing work as always.</li>
<li><a href="https://twitter.com/jsherma100" target="_blank">@jsherma100</a> published an <a href="https://jsherman212.github.io/used_sock/" target="_blank">incredibly detailed write up</a> of the iOS 12-12.2 and 12.3 user-after-free exploit that became "<a href="https://gist.github.com/ur0/a9b2d8088479a70665f729c4e9bf8720" target="_blank">Sock Puppet</a>".</li>
</ul>
</dd>
</dl>
</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.rapid7.com/2020/02/04/doublepulsar-rce-2-an-rdp-story/" target="_blank">This article</a> details the creation of the RDP variant of the DOPU metasploit module and is a great resource for anyone looking to port tools/techniques to metasploit.</li>
<li>Hexacorn shows <a href="http://www.hexacorn.com/blog/2020/02/05/stay-positive-lolbins-not/" target="_blank">how to use 32/64 bit wrapping with ordinals</a> and <a href="https://lolbas-project.github.io/" target="_blank">LOLBins</a> to avoid static detections.</li>
<li>Need a <a href="https://twitter.com/SBousseaden/status/1177131898797211654" target="_blank">potentially whitelisted spot to drop a DLL</a>? Try <code>%localapdata%assemblytmp[A-Z0-9]{8,10}Some.Microsofty.Name.DLL</code></li>
<li><a href="https://twitter.com/kmkz_security" target="_blank">@kmkz_security</a> discovered a way to <a href="https://github.com/kmkz/Pentesting/blob/14cb9433c0a02d4277404254b7906b25ed17c09a/Post-Exploitation-Cheat-Sheet#L137" target="_blank">remotely hijack an RDP session</a> without prompting or warning a connected user using a Microsoft signed binary, and without patching for multi-session RDP. Great find!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li>PHP 7.0-7.4 <a href="https://github.com/mm0r1/exploits/blob/master/php7-backtrace-bypass/exploit.php" target="_blank">UAF exploit</a> that allows running arbitrary commands (Linux only).</li>
<li>Mimikatz can now <a href="https://twitter.com/gentilkiwi/status/1226112497259876353" target="_blank">dump creds from fully up to date Chrome</a> on windows.</li>
<li><a href="https://github.com/mattifestation/WDACTools" target="_blank">WDACTools</a> - A PowerShell module to facilitate building, configuring, deploying, and auditing Windows Defender Application Control (WDAC) policies</li>
<li><dl>
<dt>Another <a href="https://github.com/bitsadmin/fakelogonscreen" target="_blank">fake logon screen</a> for post exploitation credential capture on windows.</dt>
<dd><ul>
<li>This joins <a href="https://github.com/fox-it/Invoke-CredentialPhisher" target="_blank">Invoke-CredentialPhisher</a> and</li>
<li><a href="https://github.com/BlacksunLabs/LockScream" target="_blank">LockScream</a> for macOS</li>
</ul>
</dd>
</dl>
</li>
<li>The first open source jailbreak based on checkm8 called <a href="https://github.com/LinusHenze/Fugu" target="_blank">Fugu</a> was released. It currently only supports the iPhone 7 and iPad Pro (2017), and only works on macOS. <a href="https://checkra.in/" target="_blank">checkra1n</a> works on iPhone 5s to iPhone X but is currently closed source. Checkra1n released Linux support this week. It includes a web interface (<a href="https://twitter.com/DanyL931/status/1225036017020915712" target="_blank">demo</a>) for headless devices such as the raspberry pi.</li>
<li><a href="https://twitter.com/codecolorist" target="_blank">@CodeColorist</a> released <a href="https://github.com/chichou/vscode-frida" target="_blank">vscode-firda</a>, a VS-code based GUI for using Frida to explore apps and processes on macOS.</li>
<li><dl>
<dt>A buffer overflow was discovered in sudo (CVE-2019-18634) if pwfeedback is enabled. Check with <code>sudo -l | grep pwfeedback</code>, macOS is not vulnerable by default but Linux Mint is.</dt>
<dd><ul>
<li><a href="https://github.com/Plazmaz/CVE-2019-18634" target="_blank">PoC</a></li>
<li><a href="https://dylankatz.com/Analysis-of-CVE-2019-18634/" target="_blank">Analysis</a></li>
<li><a href="https://www.sudo.ws/alerts/pwfeedback.html" target="_blank">Official Annoucement</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/0xdea/exploits/blob/master/openbsd/raptor_opensmtpd.pl" target="_blank">OpenSMTP LPE/RCE</a> (CVE-2020-7247) exploit released. This is a critical vulnerability but not a widely used mail server.</li>
<li><dl>
<dt>TeamViewer password encryption key and IV disclosed on windows; useful for post exploitation lateral movement.</dt>
<dd><ul>
<li><a href="https://whynotsecurity.com/blog/teamviewer/" target="_blank">Blog</a></li>
<li><a href="https://github.com/V1V1/DecryptTeamViewer" target="_blank">Tool (DecryptTeamViewer)</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://www.kali.org/releases/kali-linux-2020-1-release/" target="_blank">Kali 2020.1</a> released, which includes a non-root user by default, simplified installer choices, and updated themes and icons.</li>
<li><a href="https://github.com/bishopfox/dufflebag" target="_blank">Dufflebag</a> - Search exposed AWS Elastic Block Store (EBS) volumes for secrets. This technique, shown at DEF CON 27, exploits bad (non-default) configurations for persistent disks in EC2 and Dufflebag automates the complicated process to get you loot faster.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
</section>
