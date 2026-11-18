"""Independent elementary reference cases; all synthetic."""
import sys,unittest,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"analysis"))
from dynamics import beam_frequency, sdof_accelerance, duct_mode, sound_pressure_level, first_order_sensor, modal_assurance
class AnalyticalTests(unittest.TestCase):
    def test_beam_known_simply_supported(self):
        self.assertAlmostEqual(beam_frequency(1,1,1,1,1,support="simply_supported"),math.pi/2)
    def test_beam_scaling(self):
        a=beam_frequency(.1,70e9,1e-10,2700,1e-4)
        b=beam_frequency(.2,70e9,1e-10,2700,1e-4)
        self.assertAlmostEqual(a/b,4)
    def test_cantilever_second_mode_ratio(self):
        a=beam_frequency(1,1,1,1,1)
        b=beam_frequency(1,1,1,1,1,mode=2)
        self.assertAlmostEqual(b/a,6.266893,places=5)
    def test_accelerance_zero_and_high_frequency(self):
        self.assertEqual(sdof_accelerance(0,2,100,1),0)
        self.assertAlmostEqual(sdof_accelerance(1e6,2,100,1).real,.5,places=6)
    def test_accelerance_resonance(self):
        f=math.sqrt(100/2)/(2*math.pi)
        h=sdof_accelerance(f,2,100,4)
        self.assertAlmostEqual(h.real,0)
        self.assertAlmostEqual(h.imag,math.sqrt(50)/4)
    def test_duct_modes(self):
        self.assertEqual(duct_mode(.5,340),340)
        self.assertEqual(duct_mode(.5,340,2,"open_closed"),510)
    def test_calibrated_pressure_reference(self):
        self.assertAlmostEqual(sound_pressure_level(20e-6),0)
        self.assertAlmostEqual(sound_pressure_level(1),93.9794000867)
    def test_sensor_exact_step(self):
        self.assertAlmostEqual(first_order_sensor(0,1,1,1),1-math.exp(-1))
        self.assertEqual(first_order_sensor(3,42,2,0),3)
    def test_sensor_composition(self):
        x=first_order_sensor(1,3,2,.5)
        self.assertAlmostEqual(first_order_sensor(x,3,2,.5),first_order_sensor(1,3,2,1))
    def test_mac(self):
        self.assertAlmostEqual(modal_assurance([1,2],[2j,4j]),1)
        self.assertAlmostEqual(modal_assurance([1,1],[1,-1]),0)
    def test_invalid_inputs(self):
        for fn,args in [(duct_mode,(0,340)),(first_order_sensor,(0,1,0,1)),(sound_pressure_level,(0,)),(modal_assurance,([0],[1])),(sdof_accelerance,(-1,1,1,1))]:
            with self.assertRaises(ValueError):fn(*args)
if __name__=="__main__":unittest.main()
