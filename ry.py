import gc
import matplotlib.pyplot as plt
import numpy as np
##import matplotlib.axes as xiz


class  Employee(object):
    def __init__(self, name, gender, race, interviewScore = None, decision=0):
        self.name = name
        self.gender = gender
        self.race = race
        self.interviewScore = interviewScore
        self.decision = decision

e0 = Employee('Snyder', 'trans', 'URM', 38, 1)
e1 = Employee('Larson', 'trans', 'URM', 13, 1)
e2 = Employee('Lynch', 'trans', 'URM', 44, 1)
e3 = Employee('Watkins', 'trans', 'URM', 30, 1)
e4 = Employee('Hays', 'trans', 'URM', 74, 1)
e5 = Employee('Velazquez', 'trans', 'URM', 58, 1)
e6 = Employee('Sosa', 'trans', 'URM', 9, 1)
e7 = Employee('Mckay', 'trans', 'URM', 23, 1)
e8 = Employee('Olsen', 'trans', 'URM', 99, 1)
e9 = Employee('Morton', 'trans', 'URM', 47, 1)
e10 = Employee('Miranda', 'trans', 'URM', 13, 1)
e11 = Employee('Booth', 'trans', 'URM', 96, 0)
e12 = Employee('Quinn', 'trans', 'URM', 13, 1)
e13 = Employee('Figueroa', 'trans', 'URM', 29, 1)
e14 = Employee('Mayer', 'trans', 'URM', 51, 1)
e15 = Employee('Carter', 'trans', 'URM', 51, 1)
e16 = Employee('Hooper', 'trans', 'URM', 26, 1)
e17 = Employee('Kelly', 'trans', 'URM', 57, 1)
e18 = Employee('Daniels', 'trans', 'URM', 10, 1)
e19 = Employee('Lara', 'trans', 'URM', 74, 1)
e20 = Employee('Garrison', 'trans', 'URM', 72, 1)
e21 = Employee('Mckenzie', 'trans', 'URM', 65, 1)
e22 = Employee('Hensley', 'trans', 'URM', 3, 1)
e23 = Employee('Holt', 'trans', 'URM', 16, 1)
e24 = Employee('Flynn', 'trans', 'URM', 49, 0)
e25 = Employee('Lowery', 'trans', 'URM', 99, 1)
e26 = Employee('Bailey', 'trans', 'URM', 78, 1)
e27 = Employee('Pitts', 'female', 'URM', 33, 1)
e28 = Employee('Farley', 'female', 'URM', 55, 1)
e29 = Employee('Padilla', 'female', 'URM', 90, 1)
e30 = Employee('Whitney', 'female', 'URM', 35, 1)
e31 = Employee('Alvarez', 'female', 'URM', 3, 1)
e32 = Employee('Knight', 'female', 'URM', 39, 1)
e33 = Employee('Becker', 'female', 'URM', 57, 1)
e34 = Employee('Le', 'female', 'URM', 10, 0)
e35 = Employee('Vang', 'female', 'URM', 5, 0)
e36 = Employee('Bates', 'female', 'URM', 80, 0)
e37 = Employee('Bautista', 'female', 'URM', 54, 0)
e38 = Employee('Curtis', 'female', 'URM', 67, 0)
e39 = Employee('Oconnor', 'female', 'URM', 93, 0)
e40 = Employee('Espinoza', 'female', 'URM', 6, 0)
e41 = Employee('Macdonald', 'female', 'URM', 31, 0)
e42 = Employee('Patrick', 'female', 'URM', 97, 0)
e43 = Employee('Francis', 'female', 'WRM', 96, 0)
e44 = Employee('Murphy', 'female', 'WRM', 56, 0)
e45 = Employee('Buckley', 'female', 'WRM', 80, 0)
e46 = Employee('Hughes', 'female', 'WRM', 18, 0)
e47 = Employee('Grimes', 'female', 'WRM', 63, 0)
e48 = Employee('Carey', 'female', 'WRM', 19, 0)
e49 = Employee('Huffman', 'female', 'WRM', 11, 0)
e50 = Employee('Rasmussen', 'female', 'WRM', 52, 0)
e51 = Employee('Lin', 'female', 'WRM', 6, 0)
e52 = Employee('Rosario', 'female', 'WRM', 34, 0)
e53 = Employee('Orr', 'female', 'WRM', 36, 0)
e54 = Employee('Lyons', 'female', 'WRM', 60, 0)
e55 = Employee('Marshall', 'female', 'WRM', 79, 0)
e56 = Employee('Love', 'female', 'WRM', 63, 0)
e57 = Employee('Hardin', 'female', 'WRM', 70, 0)
e58 = Employee('Riley', 'female', 'WRM', 100, 0)
e59 = Employee('Wheeler', 'female', 'WRM', 82, 0)
e60 = Employee('Cline', 'female', 'WRM', 4, 0)
e61 = Employee('Frederick', 'female', 'WRM', 48, 0)
e62 = Employee('Daugherty', 'female', 'WRM', 41, 0)
e63 = Employee('Cardenas', 'female', 'WRM', 72, 0)
e64 = Employee('Burke', 'female', 'WRM', 40, 0)
e65 = Employee('Koch', 'female', 'WRM', 6, 0)
e66 = Employee('Houston', 'female', 'WRM', 77, 0)
e67 = Employee('Stevenson', 'female', 'WRM', 34, 0)
e68 = Employee('Farmer', 'female', 'WRM', 7, 0)
e69 = Employee('Warren', 'female', 'WRM', 88, 0)
e70 = Employee('Doyle', 'female', 'WRM', 76, 0)
e71 = Employee('Thompson', 'female', 'WRM', 86, 0)
e72 = Employee('Decker', 'female', 'WRM', 78, 0)
e73 = Employee('Glover', 'female', 'WRM', 88, 0)
e74 = Employee('Miller', 'female', 'WRM', 69, 0)
e75 = Employee('Buck', 'female', 'WRM', 20, 0)
e76 = Employee('Weber', 'female', 'WRM', 84, 0)
e77 = Employee('Cooper', 'female', 'WRM', 80, 0)
e78 = Employee('Stanley', 'female', 'WRM', 54, 0)
e79 = Employee('Pearson', 'female', 'URM', 72, 0)
e80 = Employee('Hancock', 'female', 'URM', 41, 0)
e81 = Employee('Fernandez', 'female', 'URM', 88, 0)
e82 = Employee('Chung', 'female', 'URM', 91, 0)
e83 = Employee('Jenkins', 'female', 'URM', 86, 0)
e84 = Employee('Hall', 'female', 'URM', 71, 0)
e85 = Employee('Simpson', 'female', 'URM', 75, 0)
e86 = Employee('Morris', 'female', 'URM', 83, 0)
e87 = Employee('Perkins', 'female', 'URM', 78, 0)
e88 = Employee('Leach', 'female', 'URM', 58, 0)
e89 = Employee('Moss', 'female', 'URM', 73, 0)
e90 = Employee('Sullivan', 'female', 'URM', 49, 0)
e91 = Employee('Fowler', 'female', 'URM', 79, 0)
e92 = Employee('Mosley', 'female', 'URM', 97, 0)
e93 = Employee('Key', 'female', 'URM', 77, 0)
e94 = Employee('Valenzuela', 'female', 'URM', 29, 0)
e95 = Employee('Escobar', 'female', 'URM', 4, 1)
e96 = Employee('Mcknight', 'female', 'URM', 35, 0)
e97 = Employee('Goodwin', 'female', 'URM', 66, 1)
e98 = Employee('Dickson', 'female', 'URM', 28, 0)
e99 = Employee('Colon', 'male', 'URM', 30, 1)
e100 = Employee('Monroe', 'male', 'URM', 5, 1)
e101 = Employee('Meyer', 'male', 'URM', 13, 1)
e102 = Employee('Williams', 'female', 'URM', 78, 0)
e103 = Employee('Wise', 'female', 'URM', 29, 0)
e104 = Employee('Griffith', 'female', 'URM', 20, 0)
e105 = Employee('Contreras', 'female', 'URM', 57, 0)
e106 = Employee('Bennett', 'female', 'URM', 70, 0)
e107 = Employee('Mendoza', 'female', 'URM', 30, 0)
e108 = Employee('Hardy', 'female', 'URM', 35, 0)
e109 = Employee('Walter', 'female', 'URM', 73, 0)
e110 = Employee('Mcpherson', 'female', 'URM', 22, 0)
e111 = Employee('Dickerson', 'female', 'URM', 82, 0)
e112 = Employee('Cruz', 'female', 'URM', 4, 0)
e113 = Employee('Carson', 'female', 'URM', 58, 0)
e114 = Employee('Galloway', 'female', 'URM', 7, 0)
e115 = Employee('Liu', 'female', 'URM', 18, 0)
e116 = Employee('Jordan', 'female', 'URM', 39, 0)
e117 = Employee('Baxter', 'female', 'URM', 9, 0)
e118 = Employee('Mays', 'female', 'URM', 18, 0)
e119 = Employee('Phillips', 'female', 'URM', 62, 0)
e120 = Employee('Mayo', 'female', 'URM', 38, 0)
e121 = Employee('Santana', 'female', 'URM', 95, 0)
e122 = Employee('Ware', 'female', 'URM', 0, 0)
e123 = Employee('Logan', 'female', 'URM', 1, 0)
e124 = Employee('Charles', 'female', 'URM', 1, 0)
e125 = Employee('Gomez', 'female', 'URM', 93, 0)
e126 = Employee('Hutchinson', 'female', 'URM', 9, 0)
e127 = Employee('Alexander', 'female', 'URM', 30, 0)
e128 = Employee('Alvarado', 'female', 'URM', 99, 0)
e129 = Employee('Allison', 'female', 'URM', 4, 0)
e130 = Employee('Webster', 'female', 'URM', 17, 0)
e131 = Employee('Mccullough', 'female', 'URM', 9, 0)
e132 = Employee('Levy', 'female', 'URM', 10, 0)
e133 = Employee('Jensen', 'female', 'URM', 43, 0)
e134 = Employee('Sutton', 'female', 'URM', 72, 0)
e135 = Employee('Zimmerman', 'female', 'URM', 23, 0)
e136 = Employee('Kirby', 'female', 'URM', 8, 0)
e137 = Employee('Shea', 'female', 'URM', 13, 0)
e138 = Employee('Lang', 'female', 'URM', 39, 0)
e139 = Employee('Trujillo', 'female', 'URM', 63, 0)
e140 = Employee('Roth', 'female', 'URM', 19, 0)
e141 = Employee('Harrington', 'female', 'WRM', 70, 0)
e142 = Employee('Salinas', 'female', 'WRM', 60, 0)
e143 = Employee('Wagner', 'female', 'WRM', 67, 0)
e144 = Employee('Frazier', 'female', 'WRM', 56, 0)
e145 = Employee('Reid', 'female', 'WRM', 86, 0)
e146 = Employee('Stuart', 'female', 'WRM', 40, 0)
e147 = Employee('Kidd', 'female', 'WRM', 22, 0)
e148 = Employee('Reilly', 'female', 'WRM', 85, 0)
e149 = Employee('Wallace', 'female', 'WRM', 13, 0)
e150 = Employee('Novak', 'female', 'WRM', 1, 0)
e151 = Employee('Lindsey', 'female', 'WRM', 85, 0)
e152 = Employee('Henderson', 'female', 'WRM', 1, 0)
e153 = Employee('Mckee', 'female', 'WRM', 95, 1)
e154 = Employee('White', 'female', 'WRM', 91, 0)
e155 = Employee('Davila', 'female', 'WRM', 67, 0)
e156 = Employee('Oconnell', 'female', 'WRM', 87, 0)
e157 = Employee('Olson', 'female', 'WRM', 78, 0)
e158 = Employee('Baldwin', 'female', 'WRM', 44, 1)
e159 = Employee('Bentley', 'female', 'WRM', 94, 1)
e160 = Employee('Harrison', 'female', 'WRM', 71, 0)
e161 = Employee('Mcclure', 'female', 'WRM', 74, 1)
e162 = Employee('Herman', 'female', 'WRM', 54, 0)
e163 = Employee('Marsh', 'female', 'WRM', 58, 0)
e164 = Employee('Christian', 'female', 'WRM', 10, 0)
e165 = Employee('Christensen', 'female', 'WRM', 70, 0)
e166 = Employee('Burnett', 'female', 'WRM', 23, 0)
e167 = Employee('Horn', 'female', 'WRM', 1, 0)
e168 = Employee('Ellis', 'female', 'WRM', 28, 0)
e169 = Employee('Lester', 'female', 'WRM', 45, 0)
e170 = Employee('Costa', 'female', 'WRM', 56, 0)
e171 = Employee('Yu', 'female', 'WRM', 49, 0)
e172 = Employee('Krause', 'female', 'WRM', 15, 0)
e173 = Employee('Gordon', 'female', 'WRM', 99, 1)
e174 = Employee('Robbins', 'female', 'WRM', 68, 0)
e175 = Employee('Cisneros', 'female', 'WRM', 38, 0)
e176 = Employee('Berry', 'female', 'WRM', 19, 0)
e177 = Employee('Wiggins', 'female', 'WRM', 52, 0)
e178 = Employee('Calhoun', 'female', 'WRM', 27, 0)
e179 = Employee('Taylor', 'male', 'WRM', 85, 1)
e180 = Employee('Walton', 'male', 'WRM', 60, 0)
e181 = Employee('Allen', 'male', 'WRM', 36, 0)
e182 = Employee('Lowe', 'male', 'WRM', 41, 0)
e183 = Employee('Murray', 'male', 'WRM', 98, 0)
e184 = Employee('Jennings', 'male', 'WRM', 64, 0)
e185 = Employee('Carpenter', 'male', 'WRM', 18, 0)
e186 = Employee('Evans', 'male', 'WRM', 36, 0)
e187 = Employee('Michael', 'male', 'WRM', 22, 0)
e188 = Employee('Roman', 'male', 'WRM', 69, 0)
e189 = Employee('Riddle', 'male', 'WRM', 28, 0)
e190 = Employee('Burton', 'male', 'WRM', 97, 0)
e191 = Employee('Pugh', 'male', 'WRM', 1, 0)
e192 = Employee('Velez', 'male', 'WRM', 27, 0)
e193 = Employee('Silva', 'male', 'WRM', 30, 0)
e194 = Employee('Stone', 'male', 'WRM', 2, 0)
e195 = Employee('Reynolds', 'male', 'WRM', 95, 1)
e196 = Employee('Harding', 'male', 'WRM', 2, 0)
e197 = Employee('Schultz', 'male', 'WRM', 49, 0)
e198 = Employee('Villegas', 'male', 'WRM', 60, 0)
e199 = Employee('Savage', 'male', 'WRM', 30, 0)
e200 = Employee('Goodman', 'male', 'WRM', 37, 0)
e201 = Employee('Garrett', 'male', 'WRM', 24, 0)
e202 = Employee('Pittman', 'male', 'WRM', 92, 0)
e203 = Employee('Esparza', 'male', 'WRM', 39, 0)
e204 = Employee('Barrett', 'male', 'WRM', 35, 0)
e205 = Employee('Proctor', 'male', 'WRM', 59, 0)
e206 = Employee('Boyd', 'male', 'WRM', 99, 1)
e207 = Employee('Nichols', 'male', 'WRM', 89, 0)
e208 = Employee('Shah', 'male', 'WRM', 84, 0)
e209 = Employee('Schroeder', 'male', 'WRM', 82, 0)
e210 = Employee('Davidson', 'male', 'WRM', 36, 0)
e211 = Employee('Chen', 'male', 'WRM', 74, 0)
e212 = Employee('Stark', 'male', 'WRM', 3, 0)
e213 = Employee('Yates', 'male', 'WRM', 75, 0)
e214 = Employee('Edwards', 'male', 'WRM', 76, 0)
e215 = Employee('Malone', 'male', 'WRM', 76, 0)
e216 = Employee('Hines', 'male', 'WRM', 10, 0)
e217 = Employee('West', 'male', 'WRM', 44, 0)
e218 = Employee('Richmond', 'male', 'WRM', 51, 0)
e219 = Employee('Singh', 'male', 'WRM', 97, 0)
e220 = Employee('Miles', 'male', 'WRM', 65, 0)
e221 = Employee('Zavala', 'male', 'WRM', 1, 0)
e222 = Employee('Hicks', 'male', 'WRM', 31, 0)
e223 = Employee('Hodges', 'male', 'WRM', 18, 0)
e224 = Employee('Acevedo', 'male', 'WRM', 45, 0)
e225 = Employee('Petty', 'male', 'WRM', 94, 0)
e226 = Employee('Mcintyre', 'male', 'WRM', 84, 0)
e227 = Employee('Hebert', 'male', 'WRM', 41, 0)
e228 = Employee('Craig', 'male', 'WRM', 36, 0)
e229 = Employee('Barajas', 'male', 'WRM', 44, 0)
e230 = Employee('Wilkins', 'male', 'WRM', 68, 0)
e231 = Employee('Haas', 'male', 'WRM', 84, 0)
e232 = Employee('Rios', 'male', 'WRM', 44, 0)
e233 = Employee('Gilbert', 'male', 'WRM', 91, 0)
e234 = Employee('Payne', 'male', 'WRM', 89, 0)
e235 = Employee('Acosta', 'male', 'WRM', 21, 0)
e236 = Employee('Hendricks', 'male', 'WRM', 98, 0)
e237 = Employee('Hale', 'male', 'WRM', 6, 0)
e238 = Employee('Jacobs', 'male', 'WRM', 9, 0)
e239 = Employee('Rocha', 'male', 'WRM', 33, 0)
e240 = Employee('Ali', 'male', 'WRM', 100, 0)
e241 = Employee('Pace', 'male', 'WRM', 14, 0)
e242 = Employee('Schmidt', 'male', 'WRM', 52, 0)
e243 = Employee('Villa', 'male', 'WRM', 44, 0)
e244 = Employee('Benton', 'male', 'WRM', 68, 0)
e245 = Employee('Arnold', 'male', 'WRM', 38, 0)
e246 = Employee('Wright', 'male', 'WRM', 64, 0)
e247 = Employee('Mullen', 'male', 'WRM', 36, 0)
e248 = Employee('Mcmahon', 'male', 'WRM', 13, 0)
e249 = Employee('Mills', 'male', 'WRM', 94, 0)
e250 = Employee('Oliver', 'male', 'WRM', 3, 0)
e251 = Employee('Lawson', 'male', 'WRM', 87, 0)
e252 = Employee('Tran', 'male', 'WRM', 53, 0)
e253 = Employee('Todd', 'male', 'WRM', 28, 0)
e254 = Employee('Newton', 'male', 'WRM', 54, 0)
e255 = Employee('Shepherd', 'male', 'WRM', 21, 0)
e256 = Employee('Cain', 'male', 'WRM', 84, 0)
e257 = Employee('Dalton', 'male', 'WRM', 52, 0)
e258 = Employee('Gallagher', 'male', 'WRM', 21, 0)
e259 = Employee('Stephenson', 'male', 'WRM', 97, 0)
e260 = Employee('Morrison', 'male', 'WRM', 88, 0)
e261 = Employee('Crosby', 'male', 'WRM', 2, 0)
e262 = Employee('Luna', 'male', 'WRM', 13, 0)
e263 = Employee('Matthews', 'male', 'WRM', 47, 0)
e264 = Employee('Wolfe', 'male', 'WRM', 100, 0)
e265 = Employee('Santos', 'male', 'WRM', 100, 0)
e266 = Employee('Hurst', 'male', 'WRM', 66, 0)
e267 = Employee('Welch', 'male', 'WRM', 15, 0)
e268 = Employee('Harmon', 'male', 'WRM', 75, 0)
e269 = Employee('Cox', 'male', 'WRM', 89, 0)
e270 = Employee('Conner', 'male', 'WRM', 36, 0)
e271 = Employee('Franklin', 'male', 'WRM', 67, 0)
e272 = Employee('Beasley', 'male', 'WRM', 14, 0)
e273 = Employee('Thornton', 'male', 'WRM', 33, 0)
e274 = Employee('Hampton', 'male', 'WRM', 88, 0)
e275 = Employee('Munoz', 'male', 'WRM', 100, 0)
e276 = Employee('Lynn', 'male', 'WRM', 92, 0)
e277 = Employee('Cochran', 'male', 'WRM', 71, 0)
e278 = Employee('Combs', 'male', 'WRM', 28, 0)
e279 = Employee('Hansen', 'male', 'WRM', 58, 0)
e280 = Employee('David', 'male', 'WRM', 10, 0)
e281 = Employee('Leon', 'male', 'WRM', 2, 0)
e282 = Employee('Nielsen', 'male', 'WRM', 77, 0)
e283 = Employee('Richard', 'male', 'WRM', 75, 0)
e284 = Employee('Choi', 'male', 'ORM', 73, 0)
e285 = Employee('Anthony', 'male', 'ORM', 39, 0)
e286 = Employee('Bridges', 'male', 'ORM', 96, 0)
e287 = Employee('Bray', 'male', 'ORM', 13, 0)
e288 = Employee('Nash', 'male', 'ORM', 16, 0)
e289 = Employee('English', 'male', 'ORM', 53, 0)
e290 = Employee('Gallegos', 'male', 'ORM', 57, 0)
e291 = Employee('Price', 'male', 'ORM', 12, 0)
e292 = Employee('Ford', 'male', 'ORM', 15, 0)
e293 = Employee('Bowen', 'male', 'ORM', 99, 0)
e294 = Employee('Mathis', 'male', 'ORM', 24, 0)
e295 = Employee('Casey', 'male', 'ORM', 35, 0)
e296 = Employee('Ellison', 'male', 'ORM', 89, 0)
e297 = Employee('Webb', 'male', 'ORM', 2, 0)
e298 = Employee('Black', 'male', 'ORM', 67, 0)
e299 = Employee('Russell', 'male', 'ORM', 10, 0)
e300 = Employee('Elliott', 'male', 'ORM', 12, 0)
e301 = Employee('Cuevas', 'male', 'ORM', 40, 0)
e302 = Employee('Castro', 'male', 'ORM', 92, 0)
e303 = Employee('Boone', 'male', 'ORM', 74, 0)
e304 = Employee('Robles', 'male', 'ORM', 87, 0)
e305 = Employee('Rosales', 'male', 'ORM', 86, 0)
e306 = Employee('Sims', 'male', 'ORM', 65, 0)
e307 = Employee('Robinson', 'male', 'ORM', 15, 0)
e308 = Employee('Randolph', 'male', 'ORM', 89, 0)
e309 = Employee('Huynh', 'male', 'ORM', 75, 0)
e310 = Employee('Hudson', 'male', 'ORM', 35, 0)
e311 = Employee('Orozco', 'male', 'ORM', 43, 0)
e312 = Employee('Mcclain', 'male', 'ORM', 20, 0)
e313 = Employee('Pena', 'male', 'ORM', 68, 0)
e314 = Employee('Montgomery', 'male', 'ORM', 6, 0)
e315 = Employee('Branch', 'male', 'ORM', 45, 0)
e316 = Employee('Pineda', 'male', 'ORM', 74, 0)
e317 = Employee('Kerr', 'male', 'ORM', 83, 0)
e318 = Employee('Livingston', 'male', 'ORM', 34, 0)
e319 = Employee('Drake', 'male', 'ORM', 27, 0)
e320 = Employee('Washington', 'male', 'ORM', 31, 0)
e321 = Employee('Stafford', 'male', 'ORM', 54, 0)
e322 = Employee('Guzman', 'male', 'ORM', 29, 0)
e323 = Employee('Owen', 'male', 'ORM', 9, 0)
e324 = Employee('Hernandez', 'male', 'ORM', 28, 0)
e325 = Employee('Callahan', 'male', 'ORM', 20, 0)
e326 = Employee('Cummings', 'male', 'ORM', 26, 0)
e327 = Employee('Avila', 'male', 'ORM', 21, 0)
e328 = Employee('Lutz', 'male', 'ORM', 58, 0)
e329 = Employee('Conrad', 'male', 'ORM', 56, 0)
e330 = Employee('Galvan', 'male', 'ORM', 74, 0)
e331 = Employee('Gamble', 'male', 'ORM', 75, 0)
e332 = Employee('Yoder', 'male', 'ORM', 34, 0)
e333 = Employee('Sawyer', 'male', 'ORM', 35, 0)
e334 = Employee('Vance', 'male', 'ORM', 92, 0)
e335 = Employee('Murillo', 'male', 'ORM', 0, 0)
e336 = Employee('Gibson', 'male', 'ORM', 37, 0)
e337 = Employee('Graham', 'male', 'ORM', 5, 0)
e338 = Employee('Maxwell', 'male', 'ORM', 61, 0)
e339 = Employee('Wade', 'male', 'ORM', 89, 0)
e340 = Employee('Warner', 'male', 'ORM', 22, 0)
e341 = Employee('Brewer', 'male', 'ORM', 36, 0)
e342 = Employee('Lloyd', 'male', 'ORM', 99, 0)
e343 = Employee('Hinton', 'male', 'ORM', 30, 0)
e344 = Employee('Rich', 'male', 'ORM', 1, 0)
e345 = Employee('Nguyen', 'male', 'ORM', 81, 0)
e346 = Employee('Knox', 'male', 'ORM', 9, 0)
e347 = Employee('Blake', 'male', 'ORM', 82, 0)
e348 = Employee('Butler', 'male', 'ORM', 31, 0)
e349 = Employee('Freeman', 'male', 'ORM', 75, 0)
e350 = Employee('Bowman', 'male', 'ORM', 42, 0)
e351 = Employee('Garcia', 'male', 'ORM', 60, 0)
e352 = Employee('Phelps', 'male', 'ORM', 3, 0)
e353 = Employee('Richards', 'male', 'ORM', 60, 0)
e354 = Employee('Moreno', 'male', 'ORM', 96, 0)
e355 = Employee('Tate', 'male', 'ORM', 43, 0)
e356 = Employee('Delacruz', 'male', 'ORM', 7, 0)
e357 = Employee('George', 'male', 'ORM', 15, 0)
e358 = Employee('Cooke', 'male', 'ORM', 89, 0)
e359 = Employee('Byrd', 'male', 'ORM', 90, 0)
e360 = Employee('Schneider', 'male', 'ORM', 89, 0)
e361 = Employee('Vaughn', 'male', 'ORM', 38, 0)
e362 = Employee('Villanueva', 'male', 'ORM', 77, 0)
e363 = Employee('Valdez', 'male', 'ORM', 83, 0)
e364 = Employee('Gross', 'male', 'ORM', 79, 0)
e365 = Employee('King', 'male', 'ORM', 32, 0)
e366 = Employee('Stokes', 'male', 'ORM', 39, 0)
e367 = Employee('Hahn', 'male', 'ORM', 31, 0)
e368 = Employee('Massey', 'male', 'ORM', 52, 0)
e369 = Employee('Cabrera', 'male', 'ORM', 35, 0)
e370 = Employee('Mccall', 'male', 'ORM', 46, 0)
e371 = Employee('Keller', 'male', 'ORM', 10, 0)
e372 = Employee('Valentine', 'male', 'ORM', 99, 0)
e373 = Employee('Holden', 'male', 'ORM', 52, 0)
e374 = Employee('Mullins', 'male', 'ORM', 56, 0)
e375 = Employee('Nunez', 'male', 'ORM', 13, 0)
e376 = Employee('Farrell', 'male', 'ORM', 88, 0)
e377 = Employee('House', 'male', 'ORM', 19, 0)
e378 = Employee('Donovan', 'male', 'ORM', 88, 0)
e379 = Employee('Spears', 'male', 'ORM', 86, 0)
e380 = Employee('Moyer', 'male', 'ORM', 36, 0)
e381 = Employee('Molina', 'male', 'ORM', 66, 0)
e382 = Employee('Weiss', 'male', 'ORM', 5, 0)
e383 = Employee('Carr', 'male', 'ORM', 54, 0)
e384 = Employee('Scott', 'male', 'ORM', 17, 0)
e385 = Employee('Eaton', 'male', 'ORM', 37, 0)
e386 = Employee('Blair', 'male', 'ORM', 12, 0)
e387 = Employee('Guerrero', 'male', 'ORM', 15, 0)
e388 = Employee('Ross', 'male', 'ORM', 27, 0)
e389 = Employee('Ibarra', 'male', 'ORM', 75, 0)
e390 = Employee('Sellers', 'male', 'ORM', 91, 0)
e391 = Employee('Salazar', 'male', 'ORM', 27, 0)
e392 = Employee('Haynes', 'male', 'ORM', 21, 0)
e393 = Employee('Jimenez', 'male', 'ORM', 68, 0)
e394 = Employee('Roy', 'male', 'ORM', 31, 0)
e395 = Employee('Strong', 'male', 'ORM', 27, 0)
e396 = Employee('Richardson', 'male', 'ORM', 18, 0)
e397 = Employee('Owens', 'male', 'ORM', 31, 0)
e398 = Employee('Barrera', 'male', 'ORM', 75, 0)
e399 = Employee('Gibbs', 'male', 'ORM', 46, 0)
e400 = Employee('Huff', 'male', 'ORM', 30, 0)
e401 = Employee('Cameron', 'male', 'ORM', 79, 0)
e402 = Employee('Duarte', 'male', 'ORM', 92, 0)
e403 = Employee('Abbott', 'male', 'ORM', 30, 0)
e404 = Employee('Horton', 'male', 'ORM', 33, 0)
e405 = Employee('Willis', 'male', 'ORM', 45, 0)
e406 = Employee('Waters', 'male', 'ORM', 18, 0)
e407 = Employee('Hess', 'male', 'ORM', 40, 0)
e408 = Employee('Dillon', 'male', 'ORM', 18, 0)
e409 = Employee('Greer', 'male', 'ORM', 17, 0)
e410 = Employee('Blankenship', 'male', 'ORM', 34, 0)
e411 = Employee('Hatfield', 'male', 'ORM', 15, 0)
e412 = Employee('Lewis', 'male', 'ORM', 55, 0)
e413 = Employee('Pacheco', 'male', 'ORM', 43, 0)
e414 = Employee('Strickland', 'male', 'ORM', 6, 0)
e415 = Employee('Kelley', 'male', 'ORM', 56, 0)
e416 = Employee('Bolton', 'male', 'ORM', 100, 0)
e417 = Employee('Howard', 'male', 'ORM', 33, 0)
e418 = Employee('Blackwell', 'male', 'ORM', 30, 0)
e419 = Employee('Gardner', 'male', 'ORM', 13, 0)
e420 = Employee('Meyers', 'male', 'ORM', 24, 0)
e421 = Employee('Shepard', 'male', 'ORM', 70, 0)
e422 = Employee('Rodgers', 'male', 'ORM', 81, 0)
e423 = Employee('Watts', 'male', 'ORM', 20, 0)
e424 = Employee('Spence', 'male', 'ORM', 98, 0)
e425 = Employee('Walls', 'male', 'ORM', 54, 0)
e426 = Employee('Woodward', 'male', 'ORM', 28, 0)
e427 = Employee('Patton', 'male', 'ORM', 54, 0)
e428 = Employee('Soto', 'male', 'ORM', 19, 0)
e429 = Employee('Swanson', 'male', 'ORM', 59, 0)
e430 = Employee('Williamson', 'male', 'ORM', 5, 0)
e431 = Employee('Perez', 'male', 'ORM', 34, 0)
e432 = Employee('Ferguson', 'male', 'ORM', 50, 0)
e433 = Employee('Burgess', 'male', 'ORM', 11, 0)
e434 = Employee('Medina', 'male', 'ORM', 0, 0)
e435 = Employee('Irwin', 'male', 'ORM', 20, 0)
e436 = Employee('Gould', 'male', 'ORM', 94, 0)
e437 = Employee('Berger', 'male', 'ORM', 78, 0)
e438 = Employee('Parks', 'male', 'ORM', 76, 0)
e439 = Employee('Patel', 'male', 'ORM', 67, 0)
e440 = Employee('Cannon', 'male', 'ORM', 8, 0)
e441 = Employee('Meza', 'male', 'ORM', 30, 0)
e442 = Employee('Martin', 'male', 'ORM', 20, 0)
e443 = Employee('Good', 'male', 'ORM', 86, 0)
e444 = Employee('Huang', 'male', 'ORM', 27, 0)
e445 = Employee('Campos', 'male', 'ORM', 69, 0)
e446 = Employee('Compton', 'male', 'ORM', 25, 0)
e447 = Employee('Shannon', 'male', 'ORM', 98, 0)
e448 = Employee('Santiago', 'male', 'ORM', 35, 0)
e449 = Employee('Parker', 'male', 'ORM', 30, 0)
e450 = Employee('Dorsey', 'male', 'ORM', 39, 0)
e451 = Employee('Thomas', 'male', 'ORM', 39, 0)
e452 = Employee('Watson', 'male', 'ORM', 8, 1)
e453 = Employee('Haney', 'male', 'ORM', 63, 1)
e454 = Employee('Coleman', 'male', 'ORM', 41, 1)
e455 = Employee('Saunders', 'male', 'ORM', 20, 1)
e456 = Employee('Simon', 'male', 'ORM', 19, 0)
e457 = Employee('Oneal', 'male', 'ORM', 14, 1)
e458 = Employee('Zamora', 'male', 'ORM', 55, 1)
e459 = Employee('Booker', 'male', 'ORM', 16, 0)
e460 = Employee('Morse', 'male', 'ORM', 9, 0)
e461 = Employee('Odom', 'male', 'ORM', 43, 0)
e462 = Employee('Mclean', 'male', 'ORM', 76, 0)
e463 = Employee('Hammond', 'male', 'ORM', 14, 0)
e464 = Employee('Zuniga', 'male', 'ORM', 2, 0)
e465 = Employee('Waller', 'male', 'ORM', 13, 0)
e466 = Employee('Holder', 'male', 'WRM', 40, 0)
e467 = Employee('Park', 'male', 'WRM', 39, 0)
e468 = Employee('Bradford', 'male', 'WRM', 66, 0)
e469 = Employee('Maddox', 'male', 'WRM', 90, 0)
e470 = Employee('Stewart', 'male', 'WRM', 91, 0)
e471 = Employee('Keith', 'male', 'WRM', 50, 0)
e472 = Employee('Sweeney', 'male', 'WRM', 10, 0)
e473 = Employee('Boyer', 'male', 'WRM', 53, 0)
e474 = Employee('Mendez', 'male', 'WRM', 98, 0)
e475 = Employee('Higgins', 'male', 'WRM', 70, 0)
e476 = Employee('Beltran', 'male', 'WRM', 60, 0)
e477 = Employee('Fox', 'male', 'WRM', 57, 0)
e478 = Employee('Ramirez', 'male', 'WRM', 95, 0)
e479 = Employee('Foley', 'male', 'WRM', 66, 0)
e480 = Employee('Benjamin', 'male', 'WRM', 38, 0)
e481 = Employee('Mata', 'male', 'WRM', 18, 0)
e482 = Employee('Cantrell', 'male', 'WRM', 7, 0)
e483 = Employee('Ayers', 'male', 'WRM', 48, 0)
e484 = Employee('Floyd', 'male', 'WRM', 29, 0)
e485 = Employee('Macias', 'male', 'WRM', 56, 0)
e486 = Employee('Young', 'male', 'WRM', 57, 0)
e487 = Employee('Rush', 'male', 'WRM', 66, 0)
e488 = Employee('Villarreal', 'male', 'WRM', 77, 0)
e489 = Employee('Townsend', 'male', 'WRM', 53, 0)
e490 = Employee('Duke', 'male', 'WRM', 1, 0)
e491 = Employee('Barr', 'male', 'WRM', 46, 0)
e492 = Employee('Werner', 'male', 'WRM', 34, 0)
e493 = Employee('Howell', 'male', 'WRM', 24, 0)
e494 = Employee('Turner', 'male', 'WRM', 79, 0)
e495 = Employee('Bender', 'male', 'WRM', 34, 0)
e496 = Employee('Maldonado', 'male', 'WRM', 59, 0)
e497 = Employee('Walsh', 'male', 'WRM', 46, 0)
e498 = Employee('Solis', 'male', 'WRM', 61, 0)
e499 = Employee('Chan', 'male', 'WRM', 2, 0)

candidates = []

for obj in gc.get_objects():
    if isinstance(obj,Employee):
        candidates.append(obj)


class Employer(object):
    def __init__(self, name):
        self.name = name
        self.rating = {}
        #self.industry = raw_input("With what industry is your company associated?")
        self.interviewees = []
        self.employees = []

        for e in candidates:
            self.interviewees.append(e)
            if e.decision == 1:
                self.employees.append(e)

    #methods to be called on employee(s)
    def interview(self, employee, score, decision=0):
        employee.interviewScore = score
        self.interviewees.append(employee)
        if decision == 1:
            self.employees.append(employee)

    def batch_interview(self, employees):
        for i in employees:
            ##this is hard-coded for now!
            self.interview(i, i.interviewScore, i.decision)

    def setPay(self, employee, rate):
        employee.payRate = rate

    def setPerformance(self, employee, score):
        employee.payRate = score

    #methods to be called on the Employer
    def fairCheck(self):
        bias = {}   # hash map for key (Candidate discriminated against) and value (number of times discriminated against)
        for e in self.employees:
            if e.race == 'ORM' or e.race == 'WRM':
                for i in self.interviewees:
                    if i.race == 'URM' and i.decision == 0: #under-represented who were not hired
                        if i.interviewScore > e.interviewScore:
                            if i in bias:
                                bias[i] += 1 #list of over-represented individuals with lower scores
                            else:
                                bias[i] = 1

        self.fairScore_race = float(len(bias)) / float(len(self.interviewees))
        self.rating['race'] = self.fairScore_race * 100
        print 'race: ' + str(self.rating['race']) + '%'

################### Check bias against women ################

        bias1 = {}
        for e in self.employees:
            if e.gender == 'male' or e.gender == 'trans': #loop through all hires who are male or trans
                for i in self.interviewees:
                    if i.gender == 'female' and i.decision == 0: # loop through un-hired females
                        if i.interviewScore > e.interviewScore: #limit to un-hired females with higher scores than hires
                            if i in bias1:
                                bias1[i] += 1 #list of over-represented individuals with lower scores
                            else:
                                bias1[i] = 1

        self.fairScore_female = float(len(bias1)) / float(len(self.interviewees))
        self.rating['female'] = self.fairScore_female * 100
        print 'female: ' + str(self.rating['female']) + '%'

################# Check bias against trans candidates #################
        bias2 = {}
        for e in self.employees:
            if e.gender == 'female' or e.gender == 'male':
                for i in self.interviewees:
                    if i.gender == 'trans' and i.decision == 0: #check if trans person was not hired
                        if i.interviewScore > e.interviewScore:
                            if i in bias2:
                                bias2[i] += 1 #list of over-represented indivduals with lower scores
                            else:
                                bias2[i] = 1

        self.fairScore_trans = float(len(bias2)) / float(len(self.interviewees))
        self.rating['trans'] = self.fairScore_trans * 100
        print 'trans: ' + str(self.rating['trans']) + '%'

google = Employer('Google')

google.fairCheck()

u = google.rating['race'],
v = google.rating['female']
w = google.rating['trans']
x = [u,v,w]

N = 3
ind = np.arange(N)
width = 0.2

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('Discrimination in Minority Recruiting by Company X')
ax.bar(0.2, u,width=0.2,color='b',align='center')
ax.bar(1.2, v,width=0.2,color='g',align='center')
ax.bar(2.2, w,width=0.2,color='r',align='center')
ax.set_ylabel('Percentage Discriminated Against')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Race', 'Women', 'Transgender') )


plt.show()