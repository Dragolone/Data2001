import graphviz

# 创建一个有向图（UML用例图通常不强调方向，但Graphviz需要用边，故采用双向箭头）
dot = graphviz.Digraph(comment='DeathOS Use-Case Diagram', format='png')

# 设置全局样式（可根据需要调整）
dot.attr('node', fontsize='10')
dot.attr('edge', fontsize='10')

# 定义系统边界 cluster
with dot.subgraph(name='cluster_DeathOS') as c:
    c.attr(style='rounded,filled', color='lightgrey', label='DeathOS')
    # 用例节点，用椭圆形表示
    c.node('UC1', 'UC-01: System Login\n& Permission Management', shape='ellipse')
    c.node('UC2', 'UC-02: Activating\nthe Superlaser', shape='ellipse')
    c.node('UC3', 'UC-03: System Security\nMonitoring & Alerts', shape='ellipse')
    c.node('UC4', 'UC-04: Managing Darth Vader’s\nBacta Tank', shape='ellipse')
    c.node('UC5', 'UC-05: Energy Distribution\n& Emergency Power Management', shape='ellipse')

# 定义演员（这里使用box形状来表示演员）
dot.node('ImperialOfficer', 'Imperial Officer', shape='box')
dot.node('SystemAdmin', 'System Administrator', shape='box')
dot.node('Commander', 'Commander', shape='box')
dot.node('SecurityOfficer', 'Security Officer', shape='box')
dot.node('MaintenanceDroid', 'Maintenance Droid', shape='box')
dot.node('MedicalDroid', 'Medical Droid', shape='box')
dot.node('ChiefEngineer', 'Chief Engineer', shape='box')

# 连接演员与各用例（按照用例描述）

## UC-01: System Login and Permission Management
dot.edge('ImperialOfficer', 'UC1')
dot.edge('SystemAdmin', 'UC1')

## UC-02: Activating the Superlaser
dot.edge('Commander', 'UC2')
dot.edge('SecurityOfficer', 'UC2')
dot.edge('SystemAdmin', 'UC2')

## UC-03: System Security Monitoring & Alerts
dot.edge('SecurityOfficer', 'UC3')
dot.edge('SystemAdmin', 'UC3')
dot.edge('MaintenanceDroid', 'UC3')

## UC-04: Managing Darth Vader’s Bacta Tank
dot.edge('MedicalDroid', 'UC4')
dot.edge('SystemAdmin', 'UC4')
dot.edge('MaintenanceDroid', 'UC4')

## UC-05: Energy Distribution & Emergency Power Management
dot.edge('SystemAdmin', 'UC5')
dot.edge('ChiefEngineer', 'UC5')
dot.edge('MaintenanceDroid', 'UC5')

# 渲染图像并输出（这一步会生成一个 "DeathOS_usecase_diagram.png" 文件）
dot.render('DeathOS_usecase_diagram', view=True)
