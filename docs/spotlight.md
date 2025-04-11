# Spotlight

## Feature of DeepTMInter

DeepTMInter specifically targets α-helical transmembrane proteins, a class notoriously underrepresented in structural databases despite their biological significance. It predicts interaction sites solely from sequence-derived features, removing the need for 3D structural input, which is often unavailable.

> DeepTMInter demonstrates biologically meaningful predictions in real membrane protein complexes, showing potential for **drug target analysis** and functional annotation.
 

## Sun's series work in drug discovery

Jianfeng Sun is spearheading a research plan dedicated to the AI-based discovery of small molecule therapeutics targeting non-coding RNAs and proteins, working in collaboration with both experimentalists and computational scientists across the globe. He has released 5 studies as in [Table 1](#tbl:jsun-sysbiol-work).

:::{table} Sun's work in drug discovery. ➵ stands for the current work.
:label: tbl:jsun-sysbiol-work
:align: center

<table border="1" cellspacing="0" cellpadding="6">
  <thead>
    <tr style="background-color:#d9d9d9;">
      <th>Field</th>
      <th>Molecule</th>
      <th>Tool name</th>
      <th>Function</th>
      <th>Technology</th>
      <th>Publication</th>
    </tr>
  </thead>
  <tbody>
    <!-- Systems Biology -->
    <tr>
      <td rowspan="3"><strong>Systems Biology</strong></td>
      <td rowspan="2">noncoding RNA</td>
      <td><strong>DeepsmirUD</strong></td>
      <td><em>drug discovery</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.3390/ijms24031878" title="DeepsmirUD">Sun et al., 2023</a>.
        <em>International Journal of Molecular Sciences</em>
      </td>
    </tr>
    <tr>
      <td><strong>DeepdlncUD</strong></td>
      <td><em>drug discovery</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.compbiomed.2023.107226" title="DeepdlncUD">Sun et al., 2023</a>.
        <em>Computers in Biology and Medicine</em>
      </td>
    </tr>
    <tr>
      <td>protein</td>
      <td><strong>Drutai</strong></td>
      <td><em>drug discovery</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.ejmech.2023.115500" title="Drutai">Sun et al., 2023</a>.
        <em>European Journal of Medicinal Chemistry</em>
      </td>
    </tr>
    <!-- Structural Biology -->
    <tr>
      <td rowspan="2"><strong>Structural Biology</strong></td>
      <td rowspan="2">protein</td>
      <td><strong>DeepHelicon</strong></td>
      <td><em>structural prediction</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.jsb.2020.107574" title="DeepHelicon">Sun and Frishman, 2020</a>.
        <em>Journal of Structural Biology</em>
      </td>
    </tr>
    <tr>
      <td style="background: -webkit-linear-gradient(20deg, #09009f, #E743D9); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"><strong>➵DeepTMInter</strong></td>
      <td><em>protein-protein interaction prediction</em></td>
      <td>Artificial intelligence</td>
      <td>
        <a href="https://doi.org/10.1016/j.csbj.2021.03.005" title="DeepTMInter">Sun and Frishman, 2021</a>.
        <em>Computational and Structural Biotechnology Journal</em>
      </td>
    </tr>
  </tbody>
</table>
:::

## Up-to-date

We updated the **DeepTMInter** program (accessed via `0.0.1`) to make it compatible with up-to-date dependencies. It vastly reduces operations from back ends of users.

## Runtime

Once intermediate files by [the external tools](#tbl:external-tool) get prepared, it runs _per protein_ in a very fast speed.