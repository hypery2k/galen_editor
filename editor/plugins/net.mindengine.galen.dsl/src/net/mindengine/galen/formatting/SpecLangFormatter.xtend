/*
 * generated by Xtext
 */
package net.mindengine.galen.formatting

import org.eclipse.xtext.formatting.impl.AbstractDeclarativeFormatter
import org.eclipse.xtext.formatting.impl.FormattingConfig
 import com.google.inject.Inject;
 import net.mindengine.galen.services.SpecLangGrammarAccess

/**
 * This class contains custom formatting description.
 * 
 * see : http://www.eclipse.org/Xtext/documentation.html#formatting
 * on how and when to use it 
 * 
 * Also see {@link org.eclipse.xtext.xtext.XtextFormattingTokenSerializer} as an example
 */
class SpecLangFormatter extends AbstractDeclarativeFormatter {

	@Inject extension SpecLangGrammarAccess
	
	override protected void configureFormatting(FormattingConfig c) {
		// add line wrapper
		c.setLinewrap(0, 1, 2).before(COMMENTRule)
	}
}
