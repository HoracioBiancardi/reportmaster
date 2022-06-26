PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE AlarmeAtivo (                    id integer primary key autoincrement,                    data date, nomeClp text, tag text, valorAtual text, valorTrigger text, descricao text);
INSERT INTO AlarmeAtivo VALUES(1,'16/02/2021 22:18:53','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0173187255859','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(2,'16/02/2021 22:18:54','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0173187255859','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(3,'16/02/2021 22:18:54','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0662479400635','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(4,'16/02/2021 22:18:54','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0452251434326','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(5,'16/02/2021 22:18:55','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9939880371094','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(6,'16/02/2021 22:18:56','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9939880371094','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(7,'16/02/2021 22:18:56','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0190906524658','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(8,'16/02/2021 22:18:57','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0621795654297','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(9,'16/02/2021 22:18:57','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0621795654297','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(10,'16/02/2021 22:18:58','3750-CL-02','TE3220_047.VAL_PV_OUT','27.041431427002','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(11,'16/02/2021 22:18:58','3750-CL-02','TE3220_047.VAL_PV_OUT','26.992151260376','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(12,'16/02/2021 22:18:59','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0588874816895','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(13,'16/02/2021 22:18:59','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0588874816895','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(14,'16/02/2021 22:19:00','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0590362548828','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(15,'16/02/2021 22:19:00','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0029125213623','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(16,'16/02/2021 22:19:01','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0107135772705','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(17,'16/02/2021 22:19:01','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0107135772705','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(18,'16/02/2021 22:19:02','3750-CL-02','TE3220_047.VAL_PV_OUT','27.067403793335','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(19,'16/02/2021 22:19:02','3750-CL-02','TE3220_047.VAL_PV_OUT','27.013729095459','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(20,'16/02/2021 22:19:03','3750-CL-02','TE3220_047.VAL_PV_OUT','27.013729095459','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(21,'16/02/2021 22:19:03','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9954452514648','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(22,'16/02/2021 22:19:04','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0598297119141','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(23,'16/02/2021 22:19:04','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0523529052734','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(24,'16/02/2021 22:19:05','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0523529052734','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(25,'16/02/2021 22:19:05','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9958019256592','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(26,'16/02/2021 22:19:06','3750-CL-02','TE3220_047.VAL_PV_OUT','27.023717880249','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(27,'16/02/2021 22:19:07','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0712089538574','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(28,'16/02/2021 22:19:07','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9947414398193','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(29,'16/02/2021 22:19:08','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9947414398193','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(30,'16/02/2021 22:19:08','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0280017852783','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(31,'16/02/2021 22:19:09','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0562496185303','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(32,'16/02/2021 22:19:09','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0174236297607','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(33,'16/02/2021 22:19:10','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0174236297607','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(34,'16/02/2021 22:19:10','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9996185302734','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(35,'16/02/2021 22:19:11','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0602531433105','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(36,'16/02/2021 22:19:12','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0511703491211','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(37,'16/02/2021 22:19:12','3750-CL-02','TE3220_047.VAL_PV_OUT','26.9959945678711','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(38,'16/02/2021 22:19:13','3750-CL-02','TE3220_047.VAL_PV_OUT','27.064603805542','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(39,'16/02/2021 22:19:13','3750-CL-02','TE3220_047.VAL_PV_OUT','27.064603805542','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(40,'16/02/2021 22:19:14','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0454959869385','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(41,'16/02/2021 22:19:14','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0123062133789','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(42,'16/02/2021 22:19:15','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0395641326904','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(43,'16/02/2021 22:19:16','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0669269561768','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(44,'16/02/2021 22:19:16','3750-CL-02','TE3220_047.VAL_PV_OUT','26.994571685791','5','TESTE');
INSERT INTO AlarmeAtivo VALUES(45,'16/02/2021 22:19:17','3750-CL-02','TE3220_047.VAL_PV_OUT','27.0737152099609','5','TESTE');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('AlarmeAtivo',45);
COMMIT;