---
title: About MagTek Tables
layout: home
parent: 
---
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
  background-color: black;
  color: white;
}
</style>

<button class="btn js-toggle-dark-mode">Preview dark color scheme</button>

<script>
const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

jtd.addEvent(toggleDarkMode, 'click', function(){
  if (jtd.getTheme() === 'dark') {
    jtd.setTheme('light');
    toggleDarkMode.textContent = 'Preview dark color scheme';
  } else {
    jtd.setTheme('dark');
    toggleDarkMode.textContent = 'Return to the light side';
  }
});
</script>


**Table 2.3-1 - MMS SLIP Wrapper**

| Offset| Value |
|:-----------:|:-----------:|
| Byte 0 | SLIP Frame Delimiter = 0xC0 |
| Byte 1 | Message Info <br> 0x00 = Direction Host to Device <br> 0x02 = Direction Device to Host <br> 0x03 = Hardware Capability Exceeded |
| Bytes 2..5 |  Length of MMS Message <br>Use big endian order |
| Bytes 6..n | MMS Message |
| Byte n+1 | SLIP Frame Delimiter = 0xC0 |

<table>
    <tr>
        <th>Content</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>List</td>
        <td><ul>
            <li>aaa</li>
            <li>bbb</li>
        </ul></td>
    </tr>
    <tr>
        <td>Code block</td>
        <td>
            <pre><code>
ccc
            </code></pre>
        </td>
    </tr>
    <tr>
        <td>Image</td>
        <td><img src="example.png"></td>
    </tr>
</table>

<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">First column **fields**</td>
<td markdown="span">Some descriptive text. This is a markdown link to [Google](http://google.com). Or see [some link](mydoc_tags).</td>
</tr>
<tr>
<td markdown="span">Second column **fields**</td>
<td markdown="span">Some more descriptive text.
</td>
</tr>
</tbody>
</table>
![alt text](image-1.png)