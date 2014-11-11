package net.mindengine.galen.dsl.tests;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.fail;
import net.mindengine.galen.SpecLangInjectorProvider;
import net.mindengine.galen.dsl.util.FileUtil;

import org.apache.log4j.Logger;
import org.eclipse.xtext.generator.IGenerator;
import org.eclipse.xtext.generator.InMemoryFileSystemAccess;
import org.eclipse.xtext.junit4.InjectWith;
import org.eclipse.xtext.junit4.XtextRunner;
import org.eclipse.xtext.junit4.util.ParseHelper;
import org.junit.Test;
import org.junit.runner.RunWith;

import com.google.inject.Inject;

@RunWith(XtextRunner.class)
@InjectWith(SpecLangInjectorProvider.class)
public class ModelTest {

	// Logger
	private static Logger LOG = Logger.getLogger(ModelTest.class);

	@Inject
	ParseHelper<net.mindengine.galen.specLang.Model> parseHelperTestDSL;

	/**
	 * Empty models should result in a null model
	 * 
	 * @throws Exception
	 */
	@Test
	public void testEmptyModel() throws Exception {
		StringBuilder emptyModelString = new StringBuilder();
		emptyModelString.append("");
		net.mindengine.galen.specLang.Model emptyTestModel = parseHelperTestDSL
				.parse(emptyModelString);
		assertNull("TestModel is not empty", emptyTestModel);
	}

	@Test
	public void testBsGeneration() throws Exception {
		// init file access
		InMemoryFileSystemAccess fsa = new InMemoryFileSystemAccess();
		// read in bs setup test file
		StringBuilder modelStringBs = FileUtil
				.readFile("src/net/mindengine/galen/dsl/testdata/model/sample1.spec");

		net.mindengine.galen.specLang.Model testModel = null;
		try {
			testModel = parseHelperTestDSL.parse(modelStringBs);
		} catch (Exception e) {
			fail("Error during parsing the test  model");
		}
		assertNotNull("test model shouldn't be null.", testModel);
	}
}
