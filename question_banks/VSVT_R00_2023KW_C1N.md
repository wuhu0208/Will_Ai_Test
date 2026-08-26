---
schema_version: will-ai-question-bank/v1
source_pdf: VSVT_R00_2023KW_C1N.pdf
source_sha256: 9584362162a9808ca4c05899055f68d839d4676c154e43a6f30940be77b4885f
source_pages: 42
question_bank_version: V1
product_scope: VS / VT / VSB / VSJ / VZ
---

# VSVT_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `VSVT_R00_2023KW_C1N.pdf`
- SHA-256: `9584362162a9808ca4c05899055f68d839d4676c154e43a6f30940be77b4885f`
- Physical pages: 42
- Product scope: VS 单动弹簧夹紧器、VT 复动夹紧器、VSB 埋入式套、VSJ 法兰式套、VS 专用 VZ 水平度调整垫片，以及直接适用于该产品族的设计、安装、操作与维护要求

## 2. Scope

本题库遵循一个 PDF 对应一个 canonical Markdown，覆盖同一托盘快换系统中的 VS、VT、VSB、VSJ 与 VS 专用 VZ 调整垫片。题目明确区分 VS 单动弹簧夹紧、VT 复动液压夹紧、套的定位功能，以及全产品族或文档共通规则；不将重复语言页、公司介绍和销售网点拆成独立题库。

### 2.1 覆盖原则

- `HIGH`：VS/VT 型号、夹紧与提升规格、套的功能组合、动作、定位精度、载荷位移、关键设计和安装边界均映射到题目。
- `MEDIUM`：VSB/VSJ 安装、VZ 调整垫片、液压回路、排气、安全与维护映射到代表题。
- `LOW/EXCLUDED`：关联产品概览、符号变更、重复语言页、公司与销售网点保留处置理由，不单独出题。

### 2.2 VS / VT 边界

- VS 是弹簧夹紧、液压释放的单动夹紧器；供给油压改变提升力，不改变弹簧夹紧力。
- VT 是液压夹紧、液压释放的复动夹紧器；夹紧力和提升力均随供给油压改变。
- `VS0250`、`VS0400` 没有 VT/WVS 共用尺寸，不得把 VS 专有尺寸外推给 VT。
- VZ `-VS1` 水平度调整垫片只适用于 VS，不得绑定到 VT。

### 2.3 图表与计算边界

- `CHART` 题使用物理页 15、17 的连续曲线视觉读数；题目输入不直接落在离散规格表给出的节点上，并设置与图像分辨率相符的读图公差。
- `TABLE` 题按物理页 15 的离散规格值精确判定，不以连续曲线公差放宽。
- `CALCULATION` 题只使用 PDF 明示的单台夹紧力和设计比例规则；十进制结果采用 `ROUND_HALF_UP`。

### 2.4 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| VSVT-SI-001 | 1-2 | 托盘快换系统概览 | TEXT | 重复定位精度、夹紧力范围、吹气清洁与着座确认；`VSVT-Q-0022` | HIGH：已映射 |
| VSVT-SI-002 | 3-4 | 应用与关联功能 | TEXT + CIRCUIT | 自动连接、断开后保压；清单保留 | MEDIUM：由核心系统题代表覆盖 |
| VSVT-SI-003 | 5-6 | VS/VT/WVS 与套的共用边界 | TABLE + TEXT | 共用尺寸和 VS 专有尺寸；`VSVT-Q-0004` | HIGH：已映射 |
| VSVT-SI-004 | 7-8 | 夹紧器与套的系统组合 | DIAGRAM + TEXT | D/C/G/F 的定位功能；`VSVT-Q-0005` | HIGH：已映射 |
| VSVT-SI-005 | 9-10 | 清洁、提升、夹紧与着座动作 | DIAGRAM + PROCEDURE | VS 动作顺序；`VSVT-Q-0006` | HIGH：已映射 |
| VSVT-SI-006 | 11-12 | 浮动分割锥套定位机理 | TEXT + DIAGRAM | 双面约束、误差吸收与零间隙；`VSVT-Q-0007` | HIGH：已映射 |
| VSVT-SI-007 | 13-14 | VS/VT/VSB/VSJ/VZ 型号表示 | MODEL + TABLE | 型号字段、力代码、法兰形状、套功能；`VSVT-Q-0001`-`0004`、`0021` | HIGH：已映射 |
| VSVT-SI-008 | 15-16 | 夹紧力/提升力规格与 VT 压力曲线 | TABLE + CHART | VS/VT 离散规格、连续曲线；`VSVT-Q-0008`-`0010`、`0012` | HIGH：已映射 |
| VSVT-SI-009 | 17-18 | VS 横向载荷位移曲线 | CHART + TEXT | 预测位移和试验条件；`VSVT-Q-0013` | HIGH：已映射 |
| VSVT-SI-010 | 19-20 | VS 外形与安装尺寸 | DRAWING + TABLE | 尺寸选型；清单保留 | MEDIUM：核心型号和安装题代表覆盖 |
| VSVT-SI-011 | 21-22 | VS 专用 VZ 调整垫片 | MODEL + CAUTION | 专用边界、螺栓与节距公差；`VSVT-Q-0024` | MEDIUM：已映射 |
| VSVT-SI-012 | 23-26 | VT 圆形/方形法兰外形 | DRAWING + TABLE | A/B 法兰与安装边界；`VSVT-Q-0002` | HIGH：已映射 |
| VSVT-SI-013 | 27-28 | VSB 埋入式套 | MODEL + DRAWING + CAUTION | 套功能、弹簧销、低刚性托盘；`VSVT-Q-0003`、`0021` | HIGH：已映射 |
| VSVT-SI-014 | 29-30 | VSJ 法兰式套 | MODEL + DRAWING + CAUTION | 套功能、弹簧销、低刚性托盘；`VSVT-Q-0003`、`0021` | HIGH：已映射 |
| VSVT-SI-015 | 31-32 | 关联液压单元和自动连接器 | TABLE + TEXT | 关联产品选择；LOW，清单保留，不单独出题 |
| VSVT-SI-016 | 33-34 | VS/VT 设计、拆装、调整和姿态限制 | PROCEDURE + CAUTION | 保护环、着座调整、导向、姿态；`VSVT-Q-0014`-`0017` | HIGH：已映射 |
| VSVT-SI-017 | 35-38 | 共通液压安装、操作与维护 | PROCEDURE + CAUTION | 回路控制、排气、清洁、安全、维护；`VSVT-Q-0018`-`0020`、`0023` | MEDIUM：已映射 |
| VSVT-SI-018 | 39-42 | 符号变更、公司与销售网点 | TEXT | 非耐久技术知识或联系信息 | EXCLUDED：不出题 |

## 3. Question Statistics

- Total: 24
- VS-specific: 9
- VT-specific: 4
- VS/VT family and sleeves: 6
- Document Common: 5
- MODEL: 3
- SPEC_LOOKUP: 5
- TABLE: 2
- CALCULATION: 2
- CHART: 2
- PROCEDURE: 5
- CAUTION: 5

## 4. Questions

## VSVT-Q-0001

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: VS 单动弹簧夹紧器
- Model / Scope: VS 型号表示、夹紧力代码与功能分类

### Question

解释 `VS0060-MD` 的系列、夹紧力代码、设计编号和功能分类，并说明功能代码 `D`、`G` 的机械含义。

### Standard Answer

`VS` 表示单动弹簧夹紧器；夹紧力代码 `06` 表示夹紧力 6.0 kN；设计编号为 `0`；`M` 是功能分类字段的固定前缀；`D` 表示锥销，承担定位并夹紧；`G` 表示直导销，承担导向并夹紧。

### Scoring Standard

- P1 [9]: `VS` 正确解释为单动弹簧夹紧器。
- P2 [9]: 正确识别夹紧力代码为 `06`。
- P3 [9]: `06` 正确对应 6.0 kN。
- P4 [9]: 设计编号正确写为 `0`。
- P5 [9]: 正确指出 `M` 为功能分类字段的固定前缀。
- P6 [9]: `D` 正确解释为锥销。
- P7 [9]: `D` 包含定位功能。
- P8 [9]: `D` 包含夹紧功能。
- P9 [9]: `G` 正确解释为直导销。
- P10 [9]: `G` 包含导向功能。
- P11 [10]: `G` 包含夹紧功能。

### Accepted Variants

- “单动夹紧器”“单动弹簧夹紧器”可等价。
- `6 kN` 与 `6.0 kN` 等价。

### Forbidden Errors

- 将 VS 解释为液压夹紧的复动夹紧器。
- 将 `G` 解释为基准定位锥销。

### Tolerance

- 型号字段和离散夹紧力精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 1287
- Section: 型号表示（夹紧器）
- Local scope path: VS > 型号表示 > 夹紧力、设计编号、功能分类
- Evidence type: MODEL
- Evidence: VS 型号图定义 `VS 0 06 0 - M D`，并逐项给出 06=6.0 kN、设计编号 0、D 锥销和 G 直导销。

## VSVT-Q-0002

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: VT 复动夹紧器
- Model / Scope: VT 型号表示、7 MPa 夹紧力、功能与法兰形状

### Question

解释 `VT0060-MD-A` 中系列、夹紧力代码、设计编号、功能代码和法兰形状，并说明可选的另一种法兰形状。

### Standard Answer

`VT` 表示复动夹紧器；代码 `06` 表示供给油压 7 MPa 时夹紧力 6.2 kN；设计编号为 `0`；功能代码 `D` 表示锥销，负责定位并夹紧；法兰代码 `A` 为圆形，另一可选代码 `B` 为方形。

### Scoring Standard

- P1 [10]: `VT` 正确解释为复动夹紧器。
- P2 [10]: 正确识别夹紧力代码为 `06`。
- P3 [10]: 正确限定额定条件为供给油压 7 MPa。
- P4 [10]: `06` 正确对应 6.2 kN。
- P5 [10]: 设计编号正确写为 `0`。
- P6 [10]: `D` 表示锥销。
- P7 [10]: `D` 包含定位功能。
- P8 [10]: `D` 包含夹紧功能。
- P9 [10]: `A` 表示圆形法兰。
- P10 [10]: `B` 表示方形法兰。

### Accepted Variants

- “圆法兰/方法兰”与“圆形/方形”可等价。

### Forbidden Errors

- 将 6.2 kN 当作 VT0060 在任意压力下恒定的夹紧力。
- 将 A、B 解释为功能分类。

### Tolerance

- 7 MPa 条件和离散规格值精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 1287
- Section: 型号表示（夹紧器）
- Local scope path: VT > 型号表示 > 夹紧力、功能分类、法兰形状
- Evidence type: MODEL
- Evidence: VT 型号图定义 `VT 0 06 0 - M D - A`，并给出 06 在 7 MPa 时为 6.2 kN、D 锥销、A 圆形和 B 方形。

## VSVT-Q-0003

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: VSB 埋入式套 / VSJ 法兰式套
- Model / Scope: 套的型号字段与功能后缀

### Question

说明 `VSB060-D` 与 `VSJ060-D` 的安装形式差异、尺寸代码和设计编号，并解释套功能后缀 `D`、`C`、`G`、`F`。

### Standard Answer

`VSB` 是埋入式套，`VSJ` 是法兰式套；两者代码 `06` 均表示匹配 06 尺寸组，设计编号均为 `0`。后缀 `D` 为锥形基准定位套，`C` 为切割套并限制一个方向，`G` 为直导套，`F` 为通用套，只提供夹紧而不提供定位或导向。

### Scoring Standard

- P1 [8]: `VSB` 正确解释为埋入式套。
- P2 [8]: `VSJ` 正确解释为法兰式套。
- P3 [8]: `06` 正确解释为匹配 06 尺寸组。
- P4 [8]: 设计编号正确写为 `0`。
- P5 [8]: `D` 为锥形基准定位套。
- P6 [8]: `C` 为切割套。
- P7 [8]: `C` 限制一个方向。
- P8 [8]: `G` 为直导套。
- P9 [9]: `F` 为通用套。
- P10 [9]: `F` 提供夹紧功能。
- P11 [9]: `F` 不提供定位功能。
- P12 [9]: `F` 不提供导向功能。

### Accepted Variants

- “埋入式/嵌入式”“法兰式/凸缘式”可按语义等价。

### Forbidden Errors

- 将 VSB 与 VSJ 视为不同尺寸编码体系。
- 声称 `F` 提供基准定位。

### Tolerance

- 型号字段精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 13-14
- Printed page: 1287-1288
- Section: 型号表示（套）
- Local scope path: VSB/VSJ > 型号表示 > 安装形式、尺寸、设计、功能
- Evidence type: MODEL
- Evidence: 型号图区分别给出 VSB 与 VSJ，并定义 D、C、G、F 的定位、导向或仅夹紧功能。

## VSVT-Q-0004

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: VS / VT / WVS 与 VSB/VSJ 套
- Model / Scope: 套尺寸组的夹紧器兼容关系

### Question

列出尺寸组 `02`、`06`、`10`、`16` 对应的 VS/VT/WVS 夹紧器，并说明 `25`、`40` 两组的兼容边界。

### Standard Answer

`02` 对应 VS0020、VS0040、VT0040、WVS0040；`06` 对应 VS0060、VT0060、WVS0060；`10` 对应 VS0100、VT0100、WVS0100；`16` 对应 VS0160、VT0160、WVS0160。`25` 只对应 VS0250，`40` 只对应 VS0400；这两个尺寸不能与 WVS 共用，也没有对应 VT 型号。

### Scoring Standard

- P1 [6]: `02` 组包含 VS0020。
- P2 [6]: `02` 组包含 VS0040。
- P3 [6]: `02` 组包含 VT0040。
- P4 [6]: `02` 组包含 WVS0040。
- P5 [6]: `06` 组包含 VS0060。
- P6 [5]: `06` 组包含 VT0060。
- P7 [5]: `06` 组包含 WVS0060。
- P8 [5]: `10` 组包含 VS0100。
- P9 [5]: `10` 组包含 VT0100。
- P10 [5]: `10` 组包含 WVS0100。
- P11 [5]: `16` 组包含 VS0160。
- P12 [5]: `16` 组包含 VT0160。
- P13 [5]: `16` 组包含 WVS0160。
- P14 [5]: `25` 组包含 VS0250。
- P15 [5]: `40` 组包含 VS0400。
- P16 [5]: VS0250 不能与 WVS 共用。
- P17 [5]: VS0400 不能与 WVS 共用。
- P18 [5]: `25` 组没有对应 VT 型号。
- P19 [5]: `40` 组没有对应 VT 型号。

### Accepted Variants

- 型号列表顺序不影响判定。

### Forbidden Errors

- 发明 VT0250、VT0400、WVS0250 或 WVS0400。

### Tolerance

- 型号与尺寸组精确匹配。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 5-6, 14
- Printed page: 1279-1280, 1288
- Section: 丰富的选择 / 型号表示（套）
- Local scope path: 产品兼容 > 套尺寸组 > VS/VT/WVS 对应型号
- Evidence type: TABLE
- Evidence: 共用说明排除 VS0250/VS0400 与 WVS，套型号表逐组列出 02、06、10、16、25、40 的适配型号。

## VSVT-Q-0005

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VS / VT 托盘快换系统
- Model / Scope: D/C/G/F 套与夹紧器组合的约束功能

### Question

分别说明夹紧器与锥套 `D`、切割套 `C`、直导套 `G`、通用套 `F` 组合后提供的约束功能。

### Standard Answer

夹紧器与 `D` 锥套组合提供基准定位和夹紧；与 `C` 切割套组合提供一个方向的定位和夹紧；与 `G` 直导套组合提供导向和夹紧；与 `F` 通用套组合只提供夹紧。

### Scoring Standard

- P1 [12]: `D` 组合提供基准定位。
- P2 [11]: `D` 组合提供夹紧。
- P3 [11]: `C` 组合提供一个方向的定位。
- P4 [11]: `C` 组合提供夹紧。
- P5 [11]: `G` 组合提供导向。
- P6 [11]: `G` 组合提供夹紧。
- P7 [11]: `F` 组合提供夹紧。
- P8 [11]: `F` 不提供定位。
- P9 [11]: `F` 不提供导向。

### Accepted Variants

- “单向定位”与“一个方向的定位”可等价。

### Forbidden Errors

- 将 `C` 说成全约束基准套。
- 将 `F` 说成导向套。

### Tolerance

- 功能映射精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 7-8
- Printed page: 1281-1282
- Section: 参考系统构成
- Local scope path: 系统构成 > 夹紧器与 D/C/G/F 套组合
- Evidence type: DIAGRAM
- Evidence: 四种组合图分别标注“定位并夹紧”“单向定位并夹紧”“导向并夹紧”“仅夹紧”。

## VSVT-Q-0006

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VS 单动弹簧夹紧器
- Model / Scope: 托盘进入、液压释放和弹簧夹紧动作

### Question

按托盘进入到夹紧完成的顺序，说明 VS 的提升防碰撞、吹气清洁、液压卸压、弹簧夹紧、定位接触和着座确认过程。

### Standard Answer

托盘进入时先在释放压力下提升，使锥形基准面与着座面之间形成间隙，避免碰撞；通过吹气清除切屑。随后去除释放压力，弹簧把拉杆向下拉，钢球把套压向着座面并形成夹紧；锥面接触完成高精度定位；最后由着座面气孔配合气密传感器确认托盘已经着座。

### Scoring Standard

- P1 [10]: 托盘进入时先在释放压力下提升。
- P2 [10]: 提升在锥形基准面与着座面之间形成间隙。
- P3 [10]: 该间隙用于避免托盘进入时碰撞。
- P4 [10]: 吹气用于清除切屑。
- P5 [10]: 去除释放压力后弹簧把拉杆向下拉。
- P6 [10]: 钢球把套压向着座面。
- P7 [10]: 套被压向着座面后形成夹紧。
- P8 [10]: 锥面接触完成高精度定位。
- P9 [10]: 着座面设有确认用气孔。
- P10 [10]: 气密传感器通过该气孔状态确认着座。

### Accepted Variants

- “卸除释放油压”与“去除释放压力”可等价。

### Forbidden Errors

- 声称 VS 通过持续夹紧油压获得夹紧力。
- 省略着座确认的气密传感器条件。

### Tolerance

- 关键动作顺序必须正确。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 9-10
- Printed page: 1283-1284
- Section: 动作说明
- Local scope path: VS > 动作 > 提升、清洁、弹簧夹紧、定位、着座确认
- Evidence type: PROCEDURE
- Evidence: 动作图与说明依次描述提升间隙、吹气、卸压后弹簧/拉杆/钢球夹紧、锥面定位和气密着座确认。

## VSVT-Q-0007

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VS / VT 定位系统
- Model / Scope: 浮动分割锥套的误差吸收与零间隙机理

### Question

说明浮动分割锥套如何实现双面约束，并列出其可吸收的四类偏差及零间隙带来的两项结果。

### Standard Answer

分割锥套通过垂直浮动，使锥形基准面与着座面同时受约束。它可吸收每个夹紧器/套的定位偏差、磨损、安装节距误差和温度变化引起的节距误差。零间隙配合带来高重复定位精度，并维持稳定的夹紧与刚性。

### Scoring Standard

- P1 [10]: 指出分割锥套可以垂直浮动。
- P2 [10]: 锥形基准面与着座面同时受约束。
- P3 [10]: 吸收夹紧器/套自身定位偏差。
- P4 [10]: 吸收磨损。
- P5 [10]: 吸收安装节距误差。
- P6 [10]: 吸收温度变化引起的节距误差。
- P7 [10]: 零间隙带来高重复定位精度。
- P8 [10]: 零间隙维持稳定夹紧。
- P9 [10]: 零间隙维持刚性。
- P10 [10]: 未把上述误差吸收错误归因于托盘滑移。

### Accepted Variants

- “上下浮动”与“垂直浮动”可等价。

### Forbidden Errors

- 声称依靠保留间隙吸收误差。

### Tolerance

- 机理和四类误差按语义精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 11-12
- Printed page: 1285-1286
- Section: 高精度定位的机构
- Local scope path: 定位机构 > 浮动分割锥套 > 双面约束、误差吸收、零间隙
- Evidence type: DIAGRAM + TEXT
- Evidence: 机构图与说明明确列出垂直移动、四类误差吸收及零间隙的定位、夹紧和刚性效果。

## VSVT-Q-0008

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: VS 单动弹簧夹紧器
- Model / Scope: 各型号夹紧力规格

### Question

按型号列出 VS0020、VS0040、VS0060、VS0100、VS0160、VS0250、VS0400 的夹紧力。

### Standard Answer

VS0020 为 2.5 kN；VS0040 为 4.0 kN；VS0060 为 6.0 kN；VS0100 为 10.0 kN；VS0160 为 16.0 kN；VS0250 为 25.0 kN；VS0400 为 40.0 kN。

### Scoring Standard

- P1 [15]: VS0020 为 2.5 kN。
- P2 [15]: VS0040 为 4.0 kN。
- P3 [14]: VS0060 为 6.0 kN。
- P4 [14]: VS0100 为 10.0 kN。
- P5 [14]: VS0160 为 16.0 kN。
- P6 [14]: VS0250 为 25.0 kN。
- P7 [14]: VS0400 为 40.0 kN。

### Accepted Variants

- 末尾 `.0` 可省略，但型号和值必须一一对应。

### Forbidden Errors

- 将提升力表中的值当作夹紧力。

### Tolerance

- 离散规格精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 15
- Printed page: 1289
- Section: 夹紧力/提升力（单动夹紧器 model VS）
- Local scope path: VS > 规格表 > 夹紧力
- Evidence type: TABLE
- Evidence: VS 规格表的夹紧力行逐型号给出 2.5、4.0、6.0、10.0、16.0、25.0、40.0 kN。

## VSVT-Q-0009

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: VT 复动夹紧器
- Model / Scope: 5 MPa 时夹紧力与提升力

### Question

列出供给油压 5 MPa 时 VT0040、VT0060、VT0100、VT0160 的夹紧力与提升力。

### Standard Answer

VT0040：夹紧力 2.9 kN、提升力 1.8 kN；VT0060：夹紧力 4.5 kN、提升力 2.9 kN；VT0100：夹紧力 7.1 kN、提升力 4.7 kN；VT0160：夹紧力 11.4 kN、提升力 7.3 kN。

### Scoring Standard

- P1 [13]: VT0040 夹紧力 2.9 kN。
- P2 [13]: VT0040 提升力 1.8 kN。
- P3 [13]: VT0060 夹紧力 4.5 kN。
- P4 [13]: VT0060 提升力 2.9 kN。
- P5 [12]: VT0100 夹紧力 7.1 kN。
- P6 [12]: VT0100 提升力 4.7 kN。
- P7 [12]: VT0160 夹紧力 11.4 kN。
- P8 [12]: VT0160 提升力 7.3 kN。

### Accepted Variants

- 可用表格作答，顺序不影响判定。

### Forbidden Errors

- 交换同一型号的夹紧力与提升力。
- 使用 7 MPa 或 3.5 MPa 行的数值。

### Tolerance

- 离散规格精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 15
- Printed page: 1289
- Section: 夹紧力/提升力（复动夹紧器 model VT）
- Local scope path: VT > 规格表 > 5 MPa 夹紧力与提升力
- Evidence type: TABLE
- Evidence: VT 规格表的 5 MPa 两行分别给出四个型号的夹紧力和提升力。

## VSVT-Q-0010

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: VS0060-MD / VS0060-MG
- Model / Scope: 2 台 MD 加 2 台 MG 的总夹紧力

### Question

某托盘使用 2 台 VS0060-MD 和 2 台 VS0060-MG。按 PDF 的单台夹紧力计算系统总夹紧力，写出公式、代入和结果。

### Standard Answer

VS0060 单台夹紧力为 6.0 kN，夹紧器总数为 `2 + 2 = 4` 台。因此总夹紧力为 `4 × 6.0 = 24.0 kN`。

### Scoring Standard

- P1 [20]: 正确查得 VS0060 单台夹紧力 6.0 kN。
- P2 [20]: 正确识别共有 4 台夹紧器。
- P3 [20]: 正确列式为 `(2 + 2) × 6.0 kN`。
- P4 [20]: 数值结果为 24.0。
- P5 [20]: 结果单位为 kN。

### Accepted Variants

- `24 kN` 与 `24.0 kN` 等价。

### Forbidden Errors

- 因 MD 与 MG 功能不同而给两者使用不同夹紧力。
- 将提升力代入计算。

### Tolerance

- 确定性计算；结果精确为 24.0 kN。
- Decimal policy: `ROUND_HALF_UP`，本题无需舍入。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 13, 15
- Printed page: 1287, 1289
- Section: 型号表示 / VS 夹紧力规格
- Local scope path: VS0060 > 功能代码 MD/MG > 单台夹紧力 > 总力计算
- Evidence type: MODEL + TABLE + FORMULA
- Evidence: MD/MG 只改变定位/导向功能；VS0060 的夹紧力规格为每台 6.0 kN。

## VSVT-Q-0011

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: VT0160
- Model / Scope: 垂直姿态允许工件重量上限

### Question

按 PDF“垂直姿态时工件或夹具板重量应在所选产品夹紧力的 10% 以内”的规则，若选用一台 VT0160，并以 7 MPa 时 16.0 kN 夹紧力校核，允许重量上限是多少？写出公式、代入和结果。

### Standard Answer

允许重量上限为夹紧力的 10%，即 `16.0 kN × 10% = 1.60 kN`。因此重量必须不大于 1.60 kN；该结果只适用于题设的一台 VT0160 和 7 MPa 条件。

### Scoring Standard

- P1 [13]: 正确引用垂直姿态 10% 规则。
- P2 [13]: 正确查得 VT0160 在 7 MPa 时夹紧力 16.0 kN。
- P3 [13]: 正确列式为 `16.0 × 0.10`。
- P4 [13]: 数值结果为 1.60。
- P5 [12]: 结果单位为 kN。
- P6 [12]: 重量边界是不大于计算值。
- P7 [12]: 结论限定于题设的一台 VT0160。
- P8 [12]: 结论限定于 7 MPa 供给油压。

### Accepted Variants

- `1.6 kN` 与 `1.60 kN` 等价。

### Forbidden Errors

- 用提升力代替夹紧力。
- 把 10% 误算为 10 倍。

### Tolerance

- 确定性计算；结果精确为 1.60 kN。
- Decimal policy: `ROUND_HALF_UP`，保留两位小数。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 15, 33
- Printed page: 1289, 1307
- Section: VT 夹紧力规格 / 垂直姿态使用注意
- Local scope path: VT0160 > 7 MPa 夹紧力 > 垂直姿态 10% 规则
- Evidence type: TABLE + FORMULA
- Evidence: VT0160 在 7 MPa 时夹紧力为 16.0 kN；设计注意规定垂直姿态重量在所选产品夹紧力 10% 以内。

## VSVT-Q-0012

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: VT0100
- Model / Scope: 6 MPa 供给油压时连续曲线读数

### Question

仅依据 VT0100 的夹紧力/提升力曲线，在供给油压 6.0 MPa 时，分别读取夹紧力（实线）和提升力（虚线）。

### Standard Answer

夹紧力约为 8.5 kN，提升力约为 5.6 kN。

### Scoring Standard

- P1 [25]: 选择 VT0100 子图。
- P2 [25]: 正确把实线识别为夹紧力。
- P3 [25]: 夹紧力读数在 8.25～8.75 kN 内。
- P4 [25]: 提升力读数在 5.35～5.85 kN 内。

### Accepted Variants

- 允许使用落在公差范围内的合理一位或两位小数读数。

### Forbidden Errors

- 直接报告 5 MPa 或 7 MPa 离散表值。
- 交换实线夹紧力与虚线提升力。

### Tolerance

- Gold: 夹紧力 8.5 kN、提升力 5.6 kN。
- Absolute tolerance: 两个读数各 ±0.25 kN。
- Boundary: 闭区间；正好落在上下界计为正确。
- 依据：图中横轴主刻度 1 MPa，纵轴主刻度 2 kN；2 倍渲染下半个小分度可稳定辨认，±0.25 kN 不宣称超出图像分辨率的精度。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 15
- Printed page: 1289
- Section: 夹紧力/提升力（复动夹紧器 model VT）
- Local scope path: VT > VT0100 曲线 > 供给油压 6.0 MPa > 实线/虚线读数
- Evidence type: CHART
- Evidence: VT0100 连续曲线以实线表示夹紧力、虚线表示提升力；6 MPa 位于 5 MPa 与 7 MPa 离散节点之间。

## VSVT-Q-0013

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: VS0100
- Model / Scope: Y 轴位移曲线，L=350 mm、F=10 kN

### Question

在 VS0100 的“对于横向载荷的变位量”图中，选择 Y 轴位移图和 `L=350 mm` 曲线；当横向载荷 `F=10 kN` 时读取位移。

### Standard Answer

Y 轴位移约为 12 μm。

### Scoring Standard

- P1 [25]: 选择 VS0100 行而不是其他型号。
- P2 [25]: 选择 Y 轴位移图而不是 X 轴位移图。
- P3 [25]: 选择 `L=350 mm` 曲线。
- P4 [25]: 读数在 11.0～13.0 μm 内。

### Accepted Variants

- 允许报告 11～13 μm 范围内的合理读图值。

### Forbidden Errors

- 使用 `L=250 mm`、`L=450 mm` 或 `L=550 mm` 曲线。
- 把读数解释为夹紧器的确定性变形上限。

### Tolerance

- Gold: 12 μm。
- Absolute tolerance: ±1.0 μm。
- Boundary: 闭区间；11.0 μm 与 13.0 μm 均计为正确。
- 依据：纵轴主刻度为 2 μm，曲线线宽和渲染分辨率不支持小于半个主刻度的强断言。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 17
- Printed page: 1291
- Section: 对于横向载荷的变位量
- Local scope path: VS0100 > Y 轴变位量 > L=350 mm > F=10 kN
- Evidence type: CHART
- Evidence: VS0100 右侧 Y 轴位移图包含 L=70、150、250、350、450、550 mm 六条曲线，L=350 曲线在 F=10 kN 处约为 12 μm。

## VSVT-Q-0014

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VS 单动弹簧夹紧器
- Model / Scope: 拆卸前保护环安装与起吊顺序

### Question

说明从设备上拆卸 VS 时，释放压力、运输保护环和起吊操作的正确顺序，并说明省略保护环的后果。

### Standard Answer

先供给释放压力，使夹紧器处于释放状态；安装运输保护环；再停止释放压力，使夹紧器回到夹紧状态。随后使用起吊螺纹使产品平行升起，并用平行销等保护螺纹端面。若未装保护环就解除约束，弹簧力可能使零件飞散，导致无法修复的损坏和人身风险。

### Scoring Standard

- P1 [9]: 首先供给释放压力。
- P2 [9]: 确认夹紧器处于释放状态。
- P3 [9]: 在释放状态安装运输保护环。
- P4 [9]: 安装保护环后停止释放压力。
- P5 [9]: 夹紧器回到夹紧状态后再起吊。
- P6 [9]: 使用起吊螺纹平行升起。
- P7 [9]: 用平行销等保护螺纹端面。
- P8 [9]: 省略保护环时弹簧力会突然释放。
- P9 [9]: 弹簧力突然释放会造成零件飞散。
- P10 [9]: 零件飞散可能造成不可修复损坏。
- P11 [10]: 零件飞散可能造成人身风险。

### Accepted Variants

- “运输用防护环”“保护环”可等价。

### Forbidden Errors

- 在未供给释放压力时强行安装或拆除保护环。
- 建议直接拉拽单侧使夹紧器倾斜起出。

### Tolerance

- 顺序必须保持“释放→装环→卸压回夹紧→平行起吊”。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 33-34
- Printed page: 1307-1308
- Section: 拆卸夹紧器 / 运输保护环
- Local scope path: VS > 拆卸 > 释放压力、保护环、起吊
- Evidence type: PROCEDURE + CAUTION
- Evidence: 拆卸图和文字明确规定保护环的安装状态、压力顺序、平行起吊方法及弹簧散件风险。

## VSVT-Q-0015

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: VSB 埋入式套
- Model / Scope: 着座面水平度调整

### Question

按顺序说明使用调整垫片把 VSB 套着座面调至推荐水平度的流程，并给出推荐值。

### Standard Answer

先装入调整垫片，再安装 VSB 套并按规定扭矩紧固；测量套着座面的水平度；拆下套和垫片，根据测量结果磨削垫片；重新装配并按规定扭矩紧固；再次测量确认。推荐水平度为 ±0.003 mm。

### Scoring Standard

- P1 [10]: 先装入调整垫片。
- P2 [10]: 安装 VSB 套。
- P3 [10]: 按规定扭矩紧固 VSB 套。
- P4 [10]: 测量着座面水平度。
- P5 [10]: 拆下 VSB 套。
- P6 [10]: 按测量结果磨削垫片。
- P7 [10]: 重新装配 VSB 套。
- P8 [10]: 重新按规定扭矩紧固。
- P9 [10]: 重新测量着座面水平度。
- P10 [10]: 推荐水平度为 ±0.003 mm。

### Accepted Variants

- “平面度/水平度”在明确指套着座面调整时可接受。

### Forbidden Errors

- 通过磨削夹紧器本体着座面代替磨削垫片。
- 省略重新装配后的复测。

### Tolerance

- 推荐值精确为 ±0.003 mm。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 33-34
- Printed page: 1307-1308
- Section: VSB 套着座面水平度调整
- Local scope path: VSB > 安装 > 调整垫片 > 测量、磨削、复测
- Evidence type: PROCEDURE
- Evidence: 安装说明逐步给出垫片装配、测量、磨削、复装和 ±0.003 mm 推荐水平度。

## VSVT-Q-0016

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VS / VT 托盘快换系统
- Model / Scope: 水平与垂直姿态的重量和防坠落边界

### Question

说明水平姿态和垂直姿态使用托盘时的重量限制，并列出垂直姿态释放时必须采取的两类防护。

### Standard Answer

水平姿态时，工件或夹具板重量不得超过产品提升力和最大承载量；垂直姿态时，重量应在所选产品夹紧力的 10% 以内。垂直释放时，如果托盘可能掉落，必须设置外部临时固定/支承；还应防止工作板或夹具板在装卡时浮起、倾斜或掉落，并定期检查因垂直使用造成的不均匀磨损和定位精度。

### Scoring Standard

- P1 [10]: 水平姿态重量不得超过提升力。
- P2 [10]: 水平姿态重量不得超过最大承载量。
- P3 [10]: 垂直姿态重量在夹紧力的 10% 以内。
- P4 [10]: 垂直释放存在掉落风险时必须设置外部临时固定。
- P5 [10]: 装卡时必须防止工作板浮起。
- P6 [10]: 装卡时必须防止工作板倾斜。
- P7 [10]: 装卡时必须防止工作板掉落。
- P8 [10]: 定期检查垂直使用造成的不均匀磨损。
- P9 [10]: 定期检查定位精度。
- P10 [10]: 夹紧器释放状态不得作为防坠落保持手段。

### Accepted Variants

- “临时支架/保持机构/外部固定”可按等效防坠措施接受。

### Forbidden Errors

- 把垂直姿态上限写为提升力的 100%。
- 认为夹紧器释放时仍能承担防坠落功能。

### Tolerance

- 比例值精确为 10%。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 1307
- Section: 注意事项（垂直姿势使用托盘）
- Local scope path: VS/VT > 姿态设计 > 重量、防坠落、磨损检查
- Evidence type: CAUTION
- Evidence: 设计注意分别规定水平姿态的提升力/承载量边界、垂直姿态的 10% 边界、临时固定及磨损检查。

## VSVT-Q-0017

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VS / VT 托盘快换系统
- Model / Scope: 粗导向、容许偏心与托盘搬入搬出

### Question

说明为什么需要设置粗导向，以及粗导向在托盘搬入/搬出时必须满足的两项运动边界。

### Standard Answer

如果超过套允许的偏心量直接搬入托盘，会损坏定位夹紧器和套，并使定位精度恶化，因此应设置粗导向。粗导向必须保证托盘在允许偏心量范围内进入，并确保托盘水平搬入、水平搬出而不发生倾斜；没有 G 导向套时还必须提供其他导向机构。

### Scoring Standard

- P1 [13]: 超过允许偏心量会损坏定位夹紧器。
- P2 [13]: 超过允许偏心量会损坏套。
- P3 [13]: 超过允许偏心量会使定位精度恶化。
- P4 [13]: 粗导向保证在允许偏心量范围内进入。
- P5 [12]: 粗导向保证托盘水平搬入。
- P6 [12]: 粗导向保证托盘水平搬出。
- P7 [12]: 粗导向防止托盘搬运时倾斜。
- P8 [12]: 没有 G 导向套时必须提供其他导向机构。

### Accepted Variants

- “预导向销/粗定位销”可等同于粗导向。

### Forbidden Errors

- 将精密锥套用作承受大偏心碰撞的粗导向。

### Tolerance

- 运动与防损伤边界按语义精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 1307
- Section: 粗导销的设置
- Local scope path: VS/VT > 托盘搬运 > 容许偏心、粗导向、水平搬运
- Evidence type: CAUTION + DIAGRAM
- Evidence: 正误图明确禁止倾斜或超偏心搬运，并要求粗导向确保允许偏心内的水平搬入搬出。

## VSVT-Q-0018

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: VSVT_R00_2023KW_C1N.pdf :: VS 单动与 VT 复动液压回路
- Model / Scope: VSVT_R00_2023KW_C1N.pdf :: 速度控制方式与单复动混合回路禁止事项

### Question

比较 VS 单动夹紧器和 VT 复动夹紧器的速度控制原则，并说明为什么不能在同一速度控制回路中混合控制两者。

### Standard Answer

VS 单动夹紧器通常使用带单向阀的流量控制阀，只控制夹紧方向；若释放负载可能造成损伤，才同时控制释放方向。VT 复动夹紧器一般在夹紧侧和释放侧均采用回油节流控制。不能在同一速度控制回路中混合 VS 与 VT，否则可能导致单动夹紧器释放动作异常或释放时间过长，应分开设置回路。

### Scoring Standard

- P1 [13]: VS 通常使用带单向阀的流量控制阀。
- P2 [13]: VS 通常只控制夹紧方向。
- P3 [13]: 只有释放负载可能造成损伤时才控制 VS 释放方向。
- P4 [13]: VT 夹紧侧一般采用回油节流。
- P5 [12]: VT 释放侧一般采用回油节流。
- P6 [12]: 混合控制可能导致 VS 释放动作异常。
- P7 [12]: 混合控制可能导致 VS 释放时间过长。
- P8 [12]: VS 与 VT 应分开设置速度控制回路。

### Accepted Variants

- “meter-out”与“回油节流”可等价。

### Forbidden Errors

- 将本文对其他特定系列的进油节流例外外推给 VT。
- 建议单动与复动夹紧器共用同一速度控制阀。

### Tolerance

- 回路控制方向按文档规则精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 35-36
- Printed page: 1309-1310
- Section: 夹紧器的速度控制回路和注意事项
- Local scope path: 共通液压安装 > 单动/复动夹紧器 > 流量控制与混合回路
- Evidence type: CIRCUIT + CAUTION
- Evidence: 共通说明分别规定单动的单向阀流控、复动的一般回油节流和禁止同回路混合速度控制。

## VSVT-Q-0019

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: VSVT_R00_2023KW_C1N.pdf :: 液压回路
- Model / Scope: VSVT_R00_2023KW_C1N.pdf :: 初次运行前排气

### Question

说明初次运行前对液压回路排气的压力限制、接头操作、排气动作、完成判据和优先位置。

### Standard Answer

把液压压力限制在 2 MPa 以下；将最靠近夹紧器的管接头螺母松开约一圈；轻轻摇动管路，使混有空气的油排出；确认排出的油不再混有气泡后重新拧紧。排气位置优先选择回路最高处或末端，也可设置排气阀。

### Scoring Standard

- P1 [15]: 排气时压力限制在 2 MPa 以下。
- P2 [15]: 松开最靠近夹紧器的管接头螺母约一圈。
- P3 [14]: 轻轻摇动管路排出含气油液。
- P4 [14]: 无气泡后重新拧紧接头。
- P5 [14]: 回路最高处是优先排气位置。
- P6 [14]: 回路末端是优先排气位置。
- P7 [14]: 可设置排气阀执行排气。

### Accepted Variants

- “不高于 2 MPa”按更保守表述接受。

### Forbidden Errors

- 在额定高压下松开接头排气。
- 完全拆下管接头。

### Tolerance

- 压力上限按 2 MPa 精确判定；“约一圈”不要求角度换算。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 35-36
- Printed page: 1309-1310
- Section: 液压回路中的空气排出
- Local scope path: 共通液压安装 > 排气 > 压力、接头、气泡、位置
- Evidence type: PROCEDURE
- Evidence: 排气步骤规定 2 MPa 以下、最近接头松一圈、摇管排气、无气泡后紧固及最高处/末端优先。

## VSVT-Q-0020

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: VSVT_R00_2023KW_C1N.pdf :: 液压配管
- Model / Scope: VSVT_R00_2023KW_C1N.pdf :: 清洁、密封带与油液要求

### Question

列出液压配管安装时对油口/管路清洁、密封带缠绕和工作油的要求，并说明违反这些要求的主要后果。

### Standard Answer

安装前必须清除油口和管路内的切屑、密封带碎片等异物；缠密封带时从管端保留 1～2 个螺纹牙，不让碎片进入回路；使用适当且清洁的 ISO VG32 液压油。异物或不合适的油液会造成内部泄漏、外部泄漏或动作不良。

### Scoring Standard

- P1 [12]: 清除油口内的切屑等异物。
- P2 [11]: 清除管路内的切屑等异物。
- P3 [11]: 防止密封带碎片进入回路。
- P4 [11]: 密封带从管端保留 1～2 个螺纹牙。
- P5 [11]: 工作油采用 ISO VG32。
- P6 [11]: 工作油必须保持清洁。
- P7 [11]: 异物可能造成内部泄漏。
- P8 [11]: 异物可能造成外部泄漏。
- P9 [11]: 异物可能造成动作不良。

### Accepted Variants

- `ISO VG 32` 与 `ISO VG32` 等价。

### Forbidden Errors

- 将密封带覆盖到管端第一牙并允许碎片进入回路。

### Tolerance

- 保留螺纹数精确为 1～2 牙。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 35-36
- Printed page: 1309-1310
- Section: 液压油 / 配管施工注意事项
- Local scope path: 共通液压安装 > 清洁、密封带、工作油
- Evidence type: CAUTION
- Evidence: 配管说明要求清洁端口、密封带留 1～2 牙并使用合适的 ISO VG32 油，警示异物导致泄漏和动作不良。

## VSVT-Q-0021

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: VSB / VSJ 套
- Model / Scope: C/G/F 功能后缀的配套限制与低刚性托盘加工

### Question

说明 VSB/VSJ 的 `C`、`G`、`F` 套在随附零件和夹紧器功能上的限制，并给出薄板或铝制低刚性托盘的孔加工建议。

### Standard Answer

只有 `C` 切割套随附弹簧销；`G` 直导套只能与功能代码 `MG` 的夹紧器配套；`F` 通用套可与 `MD` 或 `MG` 配套。薄板或铝制低刚性托盘可能因压入套而变形，孔应加工到尺寸公差上限侧，建议为 `+0.010 mm`。

### Scoring Standard

- P1 [17]: 只有 `C` 套随附弹簧销。
- P2 [17]: `G` 套只能与 `MG` 配套。
- P3 [17]: `F` 套可与 `MD` 配套。
- P4 [17]: `F` 套可与 `MG` 配套。
- P5 [16]: 低刚性托盘孔应取尺寸公差上限侧。
- P6 [16]: 低刚性托盘孔建议补偿值为 `+0.010 mm`。

### Accepted Variants

- “孔径向上公差侧加工”与“孔取上限侧”可等价，但必须包含 `+0.010 mm` 建议值。

### Forbidden Errors

- 声称 D、G 或 F 套也标配弹簧销。
- 将 G 套与 MD 作为允许的标准组合。

### Tolerance

- 建议补偿值精确为 +0.010 mm。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 27-30
- Printed page: 1301-1304
- Section: VSB / VSJ 套注意事项
- Local scope path: 套 > C/G/F 配套 > 弹簧销、功能代码、低刚性托盘
- Evidence type: SPEC_LOOKUP + CAUTION
- Evidence: VSB 与 VSJ 页重复给出 C 套弹簧销、G-MG 限制、F-MD/MG 兼容和低刚性托盘 +0.010 mm 建议。

## VSVT-Q-0022

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VS / VT 托盘快换系统
- Model / Scope: 吹气清洁、排屑结构与着座确认

### Question

说明系统如何通过吹气和结构设计防止切屑进入，并说明着座确认信号的形成方式。

### Standard Answer

托盘进入时，锥形基准面与着座面之间保持提升间隙并进行吹气清洁；防尘密封阻止异物进入；倾斜/斜面结构把切屑和冷却液排出，弹簧室与外部隔离，橡胶件保护狭缝。托盘着座后，着座面气孔的气密状态由气密传感器检测，形成着座确认信号。

### Scoring Standard

- P1 [10]: 托盘进入时形成提升间隙。
- P2 [10]: 通过提升间隙进行吹气清洁。
- P3 [10]: 防尘密封阻止异物进入。
- P4 [10]: 斜面结构排出切屑。
- P5 [10]: 斜面结构排出冷却液。
- P6 [10]: 弹簧室与外部隔离。
- P7 [10]: 橡胶件保护狭缝。
- P8 [10]: 着座面设有确认用气孔。
- P9 [10]: 气密传感器检测该气孔的气密状态。
- P10 [10]: 检测结果用于确认托盘着座。

### Accepted Variants

- “空气确认/气密检测”可等价，但必须说明着座面气孔和传感器。

### Forbidden Errors

- 声称仅靠视觉检查确认着座。
- 将吹气理解为提供夹紧力。

### Tolerance

- 结构与信号路径按语义精确判定。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 1-2, 9-10
- Printed page: 1275-1276, 1283-1284
- Section: 托盘快换系统特点 / 动作说明
- Local scope path: VS/VT > 清洁与着座确认 > 间隙、密封、排屑、气密传感器
- Evidence type: SPEC_LOOKUP + DIAGRAM
- Evidence: 系统特点与动作图描述吹气、防尘密封、排屑斜面、弹簧室隔离和气密传感器确认。

## VSVT-Q-0023

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: VSVT_R00_2023KW_C1N.pdf :: 维护检查
- Model / Scope: VSVT_R00_2023KW_C1N.pdf :: 日常与定期维护项目

### Question

列出投入使用后应执行的主要清洁、紧固、油液、动作和储存检查。

### Standard Answer

保持活塞/柱塞及定位、着座表面清洁；自动连接后若空气进入回路要排气；定期独立检查并紧固配管、安装螺栓、螺母、挡圈和夹紧件；检查液压油老化并按需要更换；检查异常声音和动作；长期停用时清洁并在干燥环境储存；需要拆修或大修时交由制造商处理。

### Scoring Standard

- P1 [9]: 清洁活塞或柱塞等外露动作表面。
- P2 [9]: 清洁定位面。
- P3 [9]: 清洁着座面。
- P4 [9]: 自动连接引入空气后执行排气。
- P5 [9]: 定期检查配管。
- P6 [9]: 定期检查机械安装紧固件。
- P7 [9]: 检查液压油老化程度。
- P8 [9]: 检查异常声音。
- P9 [9]: 检查异常动作。
- P10 [9]: 长期停用时在干燥环境储存。
- P11 [10]: 拆修或大修交由制造商处理。

### Accepted Variants

- 紧固件列表可概括，但必须同时覆盖配管和机械安装紧固件。

### Forbidden Errors

- 建议未经授权自行改造或拆修内部机构。

### Tolerance

- 维护项目按语义判定，无数值公差。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 37-38
- Printed page: 1311-1312
- Section: 维护与检查
- Local scope path: 共通维护 > 清洁、排气、紧固、油液、动作、储存
- Evidence type: PROCEDURE
- Evidence: 维护说明逐项列出清洁、空气排放、紧固检查、油液、异常动作、干燥储存和制造商大修。

## VSVT-Q-0024

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VS 专用 VZ 水平度调整垫片
- Model / Scope: 适用边界、螺栓与安装节距公差

### Question

说明 `VZ...-VS1` 水平度调整垫片的适用产品、安装螺栓要求，以及最长锥销间安装节距的公差要求。

### Standard Answer

`VZ...-VS1` 仅用于 VS 单动夹紧器，不适用于 VT。安装时不能沿用 VS 随附螺栓，因为其硬度不足；必须由用户准备满足要求的螺栓。最长锥销间安装节距应控制在 ±0.025 mm 以内。

### Scoring Standard

- P1 [17]: `-VS1` 调整垫片仅用于 VS。
- P2 [17]: `-VS1` 调整垫片不适用于 VT。
- P3 [17]: 不得沿用 VS 随附螺栓。
- P4 [17]: 禁用随附螺栓的原因是硬度不足。
- P5 [16]: 安装螺栓需由用户准备。
- P6 [16]: 最长锥销间安装节距公差为 ±0.025 mm 以内。

### Accepted Variants

- “不超过 ±0.025 mm”与“控制在 ±0.025 mm 以内”可等价。

### Forbidden Errors

- 将 `-VS1` 调整垫片用于 VT。
- 认为 VS 随附螺栓可直接用于调整垫片安装。

### Tolerance

- 节距公差边界精确为 ±0.025 mm。

### Source

- PDF: VSVT_R00_2023KW_C1N.pdf
- Physical page: 13, 21-22
- Printed page: 1287, 1295-1296
- Section: 型号表示（水平度调整垫片 VS 专用）/ 安装注意
- Local scope path: VZ...-VS1 > VS 专用 > 螺栓硬度、用户准备、最长锥销节距
- Evidence type: MODEL + CAUTION
- Evidence: 型号页明确标注 VS 专用；安装页禁止使用 VS 随附螺栓并规定最长锥销间节距 ±0.025 mm 以内。
